import requests
import json


def obter_preco(ativo):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ativo}?interval=1d&range=5d"

    headers = {
    "User-Agent": "Mozilla/5.0"
    }
    try:
            
        response = requests.get(url, headers=headers)
        dados = response.json()

        with open ('dados/Yfinance.json', 'w',encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        preco = dados["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return preco
    
    except  requests.exceptions.ConnectionError:
        print("Erro: Sem conexão com a internet ou a API caiu.")
        return None # Retorna dois Nones para evitar o erro de desempacotamento

    except KeyError:
        # Cai aqui se a moeda não existir ou se a URL errada retornar um JSON de erro
        print('Erro no KeyError')
        return None
        
    except json.JSONDecodeError:
        # Se você digitar uma URL muito errada, a API pode devolver uma página HTML
        # em vez de um JSON, o que quebra o response.json()
        print("Erro: A resposta da API não está no formato esperado.")
        return None

#======================================================================================================


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


def obter_dados(ativo):
    if ativo.endswith('.SA'):
        return obter_preco(ativo)
    else:
        return obter_cotacao(ativo)