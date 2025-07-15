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

## 🛠️ Como instalar e rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Paul-Melo/buscador-distancias.git
cd buscador-distancias
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a chave da API

**Opção A: Arquivo .env**

Crie um arquivo chamado .env na raiz do projeto e adicione:

```bash
ORS_API_KEY=sua_chave_aqui
```

**Opção B: Definir diretamente no terminal (PowerShell)**

```bash
$env:ORS_API_KEY="sua_chave_aqui"
```

### 5. Execute o script

```bash
python buscador.py
```

O script irá gerar o arquivo distancias_resultado.xlsx com as distâncias rodoviárias de Juiz de Fora e Uberlândia até as cidades listadas no Excel de entrada.

----

## 📦 Requisitos

- Python 3.10 ou superior
- Conta gratuita no openrouteservice.org

## 🛡️ Aviso sobre limites da API

Este projeto utiliza a API gratuita da OpenRouteService, que possui os seguintes limites:

- **2.000 requisições por dia**
- **40 requisições por minuto**
- **Até 1.000 destinos por chamada na API /matrix**

O script já está otimizado para respeitar essas limitações automaticamente.

## 🧠 Autor

Desenvolvido por **Paulo Melo**
- 📧 [LinkedIn](https://www.linkedin.com/in/paulo-melo-6a5683a7/)
- 💼 Portfólio (em construção)

## ✅ Licença

Este projeto está licenciado sob a **MIT License**.