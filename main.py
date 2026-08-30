from src.uteis import saudacao, calcula_estatisticas

mensagem = saudacao('Maria')
print(mensagem)

media, maximo, minimo = calcula_estatisticas([5, 10, 15])
print(f"Média: {media}, Máx: {maximo}, Mín: {minimo}")

