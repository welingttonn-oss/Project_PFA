
def somar (a,b):
    #soma(a, b) que retorna a soma.
    resultado = a + b
    return resultado



a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))

retornofunc = somar(a, b)

print(retornofunc)

#================================================================================================


def converter_dolar(real,taxa):
    #converte_dolar(real, cotacao) que retorna o valor em dólar.
    convercao = real / taxa
    return convercao

dinheiro = float(input('Digite o valor a ser convertido: '))
taxa_dolar = float(input('Digite o valor do dolar: '))


valorfinal = converter_dolar(dinheiro,taxa_dolar)

print(f'Com a taxa do dolar a USD {taxa_dolar}, convertendo R$ {dinheiro}, o valor em reais será: USD {valorfinal:.2f}')

def verifica_par_impar(numero):
    #verifica_par_impar(numero) que retorna "par" ou "ímpar".
    if numero % 2 == 0:
        return (f'Numero {numero} é par!')
    else:
        return (f'Numero {numero} é impar!')

numero = int(input('Digite um numero: ')) 

resultado = verifica_par_impar(numero)

print(resultado)
#================================================================================================



lista1 = [1,5,6,8,15,58,68,-2]
lista2 = [5,68,58,48,2,0,6,54]

def calcula_estatisticas(lista_numeros):
#Criar uma função calcula_estatisticas(lista_numeros) que retorna a média, o maior e o menor valor.
    media = sum(lista_numeros) / len(lista_numeros)
    xmax = max(lista_numeros)
    xmin = min(lista_numeros)

    return media, xmax, xmin


media, xmax, xmin = calcula_estatisticas(lista1)

#print(f'O valor médio da lista é: {media:.2f}, o valor máximo é {xmax:.2f} e o valor mínimo é: {xmin:.2f}')

#================================================================================================
def saudacao(nome, saudacao="Olá"):
#Criar uma função saudacao(nome, saudacao="Olá") que retorna a saudação personalizada.
    return f'{saudacao}, {nome}'

mensagem = saudacao(input('Digite seu nome: '))

print(mensagem)
print(f'O valor médio da lista é: {media:.2f}, o valor máximo é {xmax:.2f} e o valor mínimo é: {xmin:.2f}')


#================================================================================================

print('Listando opções de listas: \n')
print(f'Lista numero1: {lista1}')
print(f'Lista numero2: {lista2}')

try:
    opcao = int(input('Digite qual lista deseja testar: Lista1 [1], Lista2 [2] '))

    if opcao == 1:
        lista_selecionada = lista1
    elif opcao ==2:
        lista_selecionada = lista2
    else:
        print('Digite um número válido!')
        exit()
        
    media, xmax, xmin = calcula_estatisticas(lista_selecionada)

    print(f'O valor médio da lista é: {media:.2f}, o valor máximo é {xmax:.2f} e o valor mínimo é: {xmin:.2f}')
except ValueError:
    print('Só se permite numeros!')
    




#Refletir: por que usar funções em vez de escrever tudo solto?
# Entendo que quanto menos linha de código é mais fácil e organizado fica seu projeto. se entendo que um codigo pode ser reproveitado, crio uma função e nele eu sigo reutilizando. 

if __name__ == "__main__":
    # Teste local das funções
    print(saudacao("Teste"))
    print(calcula_estatisticas([1,2,3]))

    