import requests
import json


def obter_preco(ativo):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ativo}?interval=1d&range=5d"

    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    dados = response.json()

    with open ('dados/Yfinance.json', 'w',encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    preco = dados["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return preco

petrobras =  'PETR4.SA'
vale = 'VALE3.SA'

valor_petrobras = obter_preco(petrobras)
valor_vale = obter_preco(vale)

print(valor_petrobras)
print(valor_vale)