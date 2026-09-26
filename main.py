
from src.coleta import obter_preco, obter_cotacao,obter_dados # importando as funções de SRC
from src.db import criar_tabela, salvar_cotacao, listar_cotacoes, listar_ultimas
import os
from dotenv import load_dotenv #Dotenv serve para "esconder" informações importantes 
import logging # Logging serve para criar logs de execução no Sistemas
import requests

load_dotenv(override=True) # Iniciando o dotenv

#Configura o logging passando o nivel, local para salvar e formatação

logging.basicConfig( #configurando o logging
    level=logging.INFO,
    filename='logs/coleta.log',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    encoding='utf-8'
)
#ignora o retorno de logging da API
logging.getLogger("urllib3").setLevel(logging.WARNING)

logging.info('Processo iniciado!')

#pega o valor salvo no .env (escondida) e salva em uma variável
ativos = os.getenv('ATIVOS')


#Valida se a lista de ativos existe ou está vazia, caso afirmativo encerra o programa e registra no logging. se não, cria a lista separado por virgula
if ativos is None:
    logging.error('Lista de ativos não existe!')
    exit()
elif ativos == "":
    logging.warning('Lista de ativos está vazia')
    exit()
else:
    ativos_crus = ativos.split(',')

#Cria lista, faz o for ativo a ativo, "faz o tratamento de string e lança na lista de ativos_separado
ativos_separado = []

for ativo in ativos_crus:
    ativo = ativo.strip()
    if ativo != "":
        ativo = ativo.upper()
        ativos_separado.append(ativo)
#Caso a lista de ativos_separado seja vazia, encerra o programa e registra no logging.
if not ativos_separado:
    logging.warning('Lista de consulta de ativos está vazia')
    exit()

#Validando conexão com a internet: 

try:
    url = "https://www.google.com/"
    response = requests.get(url,timeout=5)
    logging.info('Conectado com a internet!')
except requests.exceptions.Timeout:
    logging.error('Conexão lenta')
    exit()
except  requests.exceptions.ConnectionError:
    logging.error('Sem conexão com a internet!')
    exit()

#Criando a tabela no financas.db 
criar_tabela()
sucessos = 0
falhas = 0


logging.info(f'Foi localizado {len(ativos_separado)} ATIVOS para consulta')


logging.info('Iniciando a coleta dos Ativos')

#Pega ativo a ativo e valida se é None, se não, chama a função para buscar na API
for i in ativos_separado:
    resultado = obter_dados(i)
    if resultado is not None:
        logging.info(f"[OK] {i}: R$ {resultado['preco']}")
        salvar_cotacao(resultado)
        sucessos += 1
#Se None, registra no log que houve uma falha e conta esta falha.
    else:
        logging.warning(f"[FALHA] {i}: não foi possível coletar")
        falhas += 1


logging.info(f'A quantidade de consultas concluidas: {sucessos}, falhas: {falhas}')


logging.info('Processo Finalizado!')


listagem = listar_ultimas(5)

if listagem is not None:
    for linha in listagem:
        id_, ativo, preco, variacao, data = linha
        logging.info(f'{ativo}: R$ {preco} {data}')
    