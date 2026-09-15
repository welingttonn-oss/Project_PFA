import sqlite3
conexao = sqlite3.connect('dados/financas.db')
cursor =  conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cotacoes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                ativo TEXT NOT NULL,
                preco REAL NOT NULL,
                variacao REAL,
                data TEXT NOT NULL

)''')

cursor.execute('''
                INSERT INTO cotacoes 
                (ativo, preco, variacao, data) VALUES
                ('VALE3.SA',6.6685,NULL,'15/09/2026 06:40:45')
''')
conexao.commit()


conexao.close()

print('funfou')