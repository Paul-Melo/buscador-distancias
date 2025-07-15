import pandas as pd
import openrouteservice
from openrouteservice import convert
from dotenv import load_dotenv
import os
import time
from tqdm import tqdm

# Carregar variáveis do .env
load_dotenv()
ORS_API_KEY = os.getenv("ORS_API_KEY")

if not ORS_API_KEY:
    raise ValueError("A variável de ambiente ORS_API_KEY não está definida.")

client = openrouteservice.Client(key=ORS_API_KEY)

# Coordenadas de referência (lon, lat)
coordenadas_referencia = {
    "Juiz_de_Fora": (-43.3397, -21.7595),
    "Uberlandia": (-48.2749, -18.914)
}

# Carregar o Excel com as cidades
df = pd.read_excel("ceps.xlsx")

# Corrigir as coordenadas para float
df['LATITUDE'] = df['LATITUDE'].astype(str).str.replace(',', '.').astype(float)
df['LONGITUDE'] = df['LONGITUDE'].astype(str).str.replace(',', '.').astype(float)

# Converter as coordenadas para o formato [lon, lat]
coordenadas_destinos = df[['LONGITUDE', 'LATITUDE']].values.tolist()

# Função para calcular distâncias com o endpoint /matrix
def calcular_distancias_matrix(origem, destinos):
    distancias = []
    BATCH_SIZE = 1000  # limite da API gratuita

    for i in range(0, len(destinos), BATCH_SIZE):
        lote = destinos[i:i + BATCH_SIZE]
        try:
            resposta = client.distance_matrix(
                locations=[origem] + lote,
                sources=[0],
                destinations=list(range(1, len(lote) + 1)),
                profile='driving-car',
                metrics=['distance'],
                units='km'
            )
            distancias.extend(resposta['distances'][0])
        except openrouteservice.exceptions.ApiError as e:
            print(f"Erro na requisição da matriz: {e}")
            distancias.extend([None] * len(lote))
            time.sleep(5)
        time.sleep(1.6)  # Respeita o limite de 40 requisições/min
    return distancias

# Processar cada cidade de referência
for nome_ref, coord_ref in coordenadas_referencia.items():
    print(f"Calculando distâncias de {nome_ref}...")
    distancias_km = calcular_distancias_matrix(coord_ref, coordenadas_destinos)
    df[f'distancia_{nome_ref}_km'] = [round(d, 2) if d else None for d in distancias_km]

# Exportar resultados
df.to_excel("distancias_resultado.xlsx", index=False)
print("Arquivo 'distancias_resultado.xlsx' criado com sucesso!")
