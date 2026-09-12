
from src.coleta import obter_preco, obter_cotacao,obter_dados


# print('Digite a opção desejada:')
# opcao = int(input('[1] para Petrobras ou [2] para Vale: '))
# if opcao == 1:
#     valorativo = 'PETR4.SA'
# elif opcao == 2:
#     valorativo = 'VALE3.SA'
# else:
#     print('Opção inválida!')



# valorativo = obter_preco('VALE3.SA')

# print(valorativo)


# moeda = input('Digite USD-BRL para saber a cotação do dolar ou EUR-BRL do euro: ')
# moeda = moeda.upper().strip()

# varBi, Bid = obter_cotacao(moeda)

# if varBi is not None and Bid is not None:
#     print(f'Cotação encontrada!')
#     print(f'Valor Bid: R$: {Bid}')
#     print(f'Variação varBid: R$: {varBi}')
# else:
#     print('Valor indevido ou moeda não encontrada!')


valor1 = obter_dados('VALE3.SA')
varBi, Bid = obter_dados('USD-BRL')

print(valor1, varBi, Bid)