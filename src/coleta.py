import requests
import json
import datetime
import logging


def obter_preco(ativo):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ativo}?interval=1d&range=5d"

    headers = {
    "User-Agent": "Mozilla/5.0"
    }
    try:
            
        response = requests.get(url, headers=headers, timeout=10)
        dados = response.json()

        with open ('dados/Yfinance.json', 'w',encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        preco = float(dados["chart"]["result"][0]["meta"]["regularMarketPrice"])
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tabela = {'ativo': ativo,
                 'preco':preco,
                  'variacao': None,
                  'data': data
                }
        return tabela
    
    except  requests.exceptions.ConnectionError:
        logging.error("Sem conexão com a internet ou a API caiu ao acessar o ativo {ativo}")
        return None# Retorna None para evitar o erro de desempacotamento

    except KeyError:
        # Cai aqui se a moeda não existir ou se a URL errada retornar um JSON de erro
        logging.error(f'Erro no KeyError ao acessar o ativo {ativo}')
        return None
        
    except json.JSONDecodeError:
        # Se você digitar uma URL muito errada, a API pode devolver uma página HTML
        # em vez de um JSON, o que quebra o response.json()
        logging.error("Erro: A resposta da API não está no formato esperado.")
        return None

#======================================================================================================


def obter_cotacao(moeda):
    if "-" not in moeda:
        moeda = f'{moeda}-BRL'
        
    moeda_json = moeda.replace("-","")
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}"

    # O 'try' começa ANTES de acessar a internet
    try:
        response = requests.get(url,timeout=10)
        dados = response.json()

        with open ('dados/awasome.json', 'w', encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
        varBi = float(dados[moeda_json]["varBid"])
        Bid = float(dados[moeda_json]["bid"])
        data = dados[moeda_json]["create_date"]
        tabela = {'ativo': moeda,
                 'preco':Bid,
                  'variacao': varBi,
                  'data': data
                }
        
        return tabela
        
    except requests.exceptions.ConnectionError:
        logging.error("Sem conexão com a internet ou a API caiu.")
        return None # Retorna None para evitar o erro de desempacotamento
        
    except KeyError:
        # Cai aqui se a moeda não existir ou se a URL errada retornar um JSON de erro
        logging.error(f"KeyError ao coletar {moeda}")

        return None
        
    except json.JSONDecodeError:
        # Se você digitar uma URL muito errada, a API pode devolver uma página HTML
        # em vez de um JSON, o que quebra o response.json()
        logging.error("A resposta da API não está no formato esperado.")
        return None


def obter_dados(ativo):
    if ativo.endswith('.SA'):
        return obter_preco(ativo)
    else:
        return obter_cotacao(ativo)