# Buscador de Distâncias Rodoviárias com OpenRouteService

Este projeto em Python calcula distâncias rodoviárias entre cidades usando a API do OpenRouteService, processando grandes volumes de dados a partir de uma planilha Excel com coordenadas.

## Funcionalidades

- Processa milhares de coordenadas em lote.
- Respeita limites de requisições da API (rate limit e limite diário).
- Continua o processamento de onde parou em execuções subsequentes.
- Gera arquivo Excel com distâncias calculadas.
- Registro de logs para acompanhamento e diagnóstico.
- Barra de progresso para feedback visual.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - pandas
  - openrouteservice
  - tqdm

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/buscador-distancias.git
cd buscador-distancias
