import os
from dotenv import load_dotenv
load_dotenv()

Ativos = os.getenv('ATIVOS')
emails = os.getenv('EMAIL_DESTINATARIO')

print(Ativos)
print(emails)
lista_ativos = Ativos.split(',')

print(lista_ativos)