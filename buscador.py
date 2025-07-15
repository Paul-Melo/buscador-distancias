import pandas as pd
import openrouteservice
import os
import time
import logging
from tqdm import tqdm

# Configuração do logging
logging.basicConfig(
    filename='processamento.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

ORS_API_KEY = "SUA_CHAVE_REAL"
client = openrouteservice.Client(key=ORS_API_KEY)

coordenadas_referencia = {
    "Juiz_de_Fora": (-21.7595, -43.3397),
    "Uberlandia": (-18.914, -48.2749)
}

ARQUIVO_ENTRADA = "ceps.xlsx"
ARQUIVO_SAIDA = "distancias_resultado.xlsx"
LIMITE_REQUISICOES = 2000
requisicoes_realizadas = 0

def calcular_distancia(origem, destino):
    global requisicoes_realizadas
    if requisicoes_realizadas >= LIMITE_REQUISICOES:
        return None

    try:
        resposta = client.directions(
            coordinates=[origem[::-1], destino[::-1]],
            profile='driving-car',
            format='geojson'
        )
        distancia_km = resposta['features'][0]['properties']['summary']['distance'] / 1000
        requisicoes_realizadas += 1
        time.sleep(1.6)
        return round(distancia_km, 2)
    except Exception as e:
        logging.error(f"Erro ao calcular distância entre {origem} e {destino}: {e}")
        return None

df_original = pd.read_excel(ARQUIVO_ENTRADA)
df_original['LATITUDE'] = df_original['LATITUDE'].astype(str).str.replace(',', '.').astype(float)
df_original['LONGITUDE'] = df_original['LONGITUDE'].astype(str).str.replace(',', '.').astype(float)

if os.path.exists(ARQUIVO_SAIDA):
    df_resultado = pd.read_excel(ARQUIVO_SAIDA)
    logging.info("Arquivo existente carregado. Continuando processamento...")
else:
    df_resultado = df_original.copy()
    for cidade_ref in coordenadas_referencia:
        df_resultado[f'distancia_{cidade_ref}_km'] = None
    logging.info("Arquivo de saída criado. Iniciando processamento...")

# Preparar a lista de índices a processar
indices_para_processar = [
    i for i, row in df_resultado.iterrows()
    if not all(pd.notnull(row[f'distancia_{cidade_ref}_km']) for cidade_ref in coordenadas_referencia)
]

# Barra de progresso com tqdm
for i in tqdm(indices_para_processar, desc="Calculando distâncias"):
    row = df_resultado.loc[i]

    coord_destino = (row['LATITUDE'], row['LONGITUDE'])

    for cidade_ref, coord_ref in coordenadas_referencia.items():
        col = f'distancia_{cidade_ref}_km'
        if pd.isnull(df_resultado.at[i, col]):
            distancia = calcular_distancia(coord_ref, coord_destino)
            df_resultado.at[i, col] = distancia

            if requisicoes_realizadas >= LIMITE_REQUISICOES:
                logging.info(f"Limite de {LIMITE_REQUISICOES} requisições atingido. Salvando progresso...")
                break

    if requisicoes_realizadas >= LIMITE_REQUISICOES:
        break

df_resultado.to_excel(ARQUIVO_SAIDA, index=False)
logging.info(f"Processamento salvo com sucesso no arquivo '{ARQUIVO_SAIDA}'.")
print(f"Processamento salvo com sucesso no arquivo '{ARQUIVO_SAIDA}'.")
