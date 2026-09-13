
from src.coleta import obter_preco, obter_cotacao,obter_dados
import os
from dotenv import load_dotenv
load_dotenv()
ativos = os.getenv('ATIVOS')


print('Digite a opção desejada:')
opcao = int(input('[1] para Petrobras ou [2] para Vale: '))
if opcao == 1:
    valorativo = 'PETR4.SA'
elif opcao == 2:
    valorativo = 'VALE3.SA'
else:
    print('Opção inválida!')



valorativo = obter_preco('VALE3.SA')

print(valorativo)


moeda = input('Digite USD-BRL para saber a cotação do dolar ou EUR-BRL do euro: ')
moeda = moeda.upper().strip()

varBi, Bid = obter_cotacao(moeda)

if varBi is not None and Bid is not None:
    print(f'Cotação encontrada!')
    print(f'Valor Bid: R$: {Bid}')
    print(f'Variação varBid: R$: {varBi}')
else:
    print('Valor indevido ou moeda não encontrada!')

escolha = 'VALE3.SA'
escolha1 = 'USD'

tabela = obter_dados(escolha)
tabela2 = obter_dados(escolha1)
print(tabela)
print(tabela2)
print('Ok')