
from src.coleta import obter_preco, obter_cotacao,obter_dados # importando as funções de SRC
from src.db import criar_tabela, salvar_cotacao, listar_cotacoes, listar_ultimas
import os
from dotenv import load_dotenv #Dotenv serve para "esconder" informações importantes 
import logging # Logging serve para criar logs de execução no Sistemas
import requests

load_dotenv(override=True) # Iniciando o dotenv

#Configura o logging passando o nivel, local para salvar e fortamatação

logging.basicConfig( #configurando o logging
    level=logging.INFO,
    filename='logs/coleta.log',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    encoding='utf-8'
)
#ignora o tetorno de logging da API
logging.getLogger("urllib3").setLevel(logging.WARNING)


listagem = listar_ultimas(-5)

if listagem is not None:
    for linha in listagem:
        id_, ativo, preco, variacao, data = linha
        logging.info(f'{ativo}: R$ {preco} {data}')

listagem = listar_ultimas(5)

if listagem is not None:
    for linha in listagem:
        id_, ativo, preco, variacao, data = linha
        logging.info(f'{ativo}: R$ {preco} {data}')