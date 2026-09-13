
from src.coleta import obter_preco, obter_cotacao,obter_dados
import os
from dotenv import load_dotenv
load_dotenv()
ativos = os.getenv('ATIVOS')

sucessos = 0
falhas = 0

ativos_separado = ativos.split(',')

print(ativos_separado)

for i in ativos_separado:
    resultado = obter_dados(i)
    if resultado is not None:
        print(f"[OK] {i}: R$ {resultado['preco']}")
        sucessos += 1
    else:
        print(f"[FALHA] {i}: não foi possível coletar")
        falhas += 1


print(f'A quantidade de consultas concluidas: {sucessos}, falhas: {falhas}')
