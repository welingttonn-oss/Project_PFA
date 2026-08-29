
def somar (a,b):
    #soma(a, b) que retorna a soma.
    resultado = a + b
    return resultado



a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))

retornofunc = somar(a, b)

print(retornofunc)



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

#Refletir: por que usar funções em vez de escrever tudo solto?
# Entendo que quanto menos linha de código é mais fácil e organizado fica seu projeto. se entendo que um codigo pode ser reproveitado, crio uma função e nele eu sigo reutilizando. 