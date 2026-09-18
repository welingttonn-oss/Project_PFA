
from src.coleta import obter_preco, obter_cotacao,obter_dados # importando as funções de SRC
from src.db import criar_tabela, salvar_cotacao, listar_cotacoes
import os
from dotenv import load_dotenv #Dotenv serve para "esconder" informações importantes 
import logging # Logging serve para criar logs de execução no Sistemas
load_dotenv() # Iniciando o dotenv


logging.basicConfig( #configurando o logging
    level=logging.INFO,
    filename='logs/coleta.log',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    encoding='utf-8'
)
logging.getLogger("urllib3").setLevel(logging.WARNING)

logging.info('Processo iniciado!')

ativos = os.getenv('ATIVOS')

criar_tabela()
sucessos = 0
falhas = 0

ativos_separado = ativos.split(',')
logging.info(f'Foi localizado {len(ativos_separado)} ATIVOS para consulta')


logging.info('Iniciando a coleta dos Ativos')

for i in ativos_separado:
    resultado = obter_dados(i)
    if resultado is not None:
        logging.info(f"[OK] {i}: R$ {resultado['preco']}")
        salvar_cotacao(resultado)
        sucessos += 1
    else:
        logging.warning(f"[FALHA] {i}: não foi possível coletar")
        falhas += 1


logging.info(f'A quantidade de consultas concluidas: {sucessos}, falhas: {falhas}')

print()

logging.info('Processo Finalizado!')



