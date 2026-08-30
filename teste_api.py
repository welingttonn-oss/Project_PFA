import requests
import json

# url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
# response = requests.get(url)


# dados = response.json()

# localdados = 'dados/awasome.json'

# with open (localdados, 'w', encoding="utf-8") as arquivo:
#     json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# print('Json salvo!')


# print(dados["USDBRL"]["bid"])
# print(dados["USDBRL"]["varBid"])

def obter_cotacao(moeda):

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
    response = requests.get(url)
    dados = response.json()
    moeda_json = moeda.replace("-","")

    with open ('dados/awasome.json', 'w', encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    varBi = dados[moeda_json]["varBid"]
    Bid = dados[moeda_json]["bid"]

    return varBi, Bid


moeda = input('Digite USD-BRL para saber a cotação do dolar ou EUR-BRL do euro: ')
moeda = moeda.upper().strip()

varBi, Bid = obter_cotacao(moeda)

print(varBi, Bid)



