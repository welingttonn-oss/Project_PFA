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
    if "-" not in moeda:
        moeda = f'{moeda}-BRL'
        
    moeda_json = moeda.replace("-","")
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    # O 'try' começa ANTES de acessar a internet
    try:
        response = requests.get(url)
        dados = response.json()

        with open ('dados/awasome.json', 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
        varBi = dados[moeda_json]["varBid"]
        Bid = dados[moeda_json]["bid"]
        
        return varBi, Bid
        
    except requests.exceptions.ConnectionError:
        print("Erro: Sem conexão com a internet ou a API caiu.")
        return None, None # Retorna dois Nones para evitar o erro de desempacotamento
        
    except KeyError:
        # Cai aqui se a moeda não existir ou se a URL errada retornar um JSON de erro
        return None, None
        
    except json.JSONDecodeError:
        # Se você digitar uma URL muito errada, a API pode devolver uma página HTML
        # em vez de um JSON, o que quebra o response.json()
        print("Erro: A resposta da API não está no formato esperado.")
        return None, None

moeda = input('Digite USD-BRL para saber a cotação do dolar ou EUR-BRL do euro: ')
moeda = moeda.upper().strip()

varBi, Bid = obter_cotacao(moeda)

if varBi is not None and Bid is not None:
    print(f'Cotação encontrada!')
    print(f'Valor Bid: R$: {Bid}')
    print(f'Variação varBid: R$: {varBi}')
else:
    print('Valor indevido ou moeda não encontrada!')





