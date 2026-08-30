
lista1 = [1,5,6,8,15,58,68,-2]
lista2 = [5,68,58,48,2,0,6,54]

def calcula_estatisticas(lista_numeros):
#Criar uma função calcula_estatisticas(lista_numeros) que retorna a média, o maior e o menor valor.
    media = sum(lista_numeros) / len(lista_numeros)
    xmax = max(lista_numeros)
    xmin = min(lista_numeros)

    return media, xmax, xmin


#================================================================================================
def saudacao(nome, saudacao="Olá"):
#Criar uma função saudacao(nome, saudacao="Olá") que retorna a saudação personalizada.
    return f'{saudacao}, {nome}'

if __name__ == "__main__":
    # Teste local das funções
    print(saudacao("Teste"))
    print(calcula_estatisticas([1,2,3]))

    