# Buscador de Distâncias com OpenRouteService

Este projeto calcula a distância rodoviária entre cidades brasileiras e duas cidades de referência: **Juiz de Fora** e **Uberlândia**, utilizando a API do [OpenRouteService](https://openrouteservice.org/).

A entrada é uma planilha `.xlsx` contendo as coordenadas (latitude e longitude) de várias cidades, e a saída é outra planilha com as distâncias em quilômetros.

---

## 🚀 Funcionalidades

- Processamento em lote de milhares de cidades
- Otimizado usando o endpoint `/matrix` do OpenRouteService (até 1000 destinos por chamada)
- Respeita limites de taxa da API gratuita
- Código estruturado para uso profissional ou acadêmico

---

## 📂 Estrutura Esperada do Arquivo de Entrada

O arquivo `ceps.xlsx` deve conter pelo menos as seguintes colunas:

- `LATITUDE` (ex: `-21.7595`)
- `LONGITUDE` (ex: `-43.3397`)

*Certifique-se de que as colunas estejam no formato numérico (ponto decimal, não vírgula).*

---

## ⚙️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/Paul-Melo/buscador-distancias.git
cd buscador-distancias
