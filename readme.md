# Golden Raspberry Awards API

## Pré-requisitos
- Python 3.10+
- pip

## Instalação
1. Clone este repositório
2. Acesse o diretório: `cd Outsera`
3. Instale as dependências com: `pip install -r requirements.txt`

## Como Rodar
1. Execute a aplicação: `python run.py`
2. Acesse o endpoint: `http://127.0.0.1:5000/api/produtoras/intervalo_premiacoes`

## Como Executar os Testes
1. Execute: `pytest tests/`

## Endpoint
- **GET /api/produtoras/intervalo_premiacoes**
  - Retorna os produtores com maior e menor intervalo entre prêmios.