import sqlite3
import logging


def criar_tabela():
    conexao = sqlite3.connect('dados/financas.db')
    cursor = conexao.cursor()
    try:

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS 
                        cotacoes (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        ativo TEXT NOT NULL,
                        preco REAL NOT NULL,
                        variacao REAL,
                        data TEXT NOT NULL            
                        )
            ''')
        conexao.commit()

        
        logging.info('Tabela criada com sucesso.')
    except Exception as e:
        logging.error(f'Erro na criação da Tabela: {e}')
    finally:
        conexao.close()


def salvar_cotacao(dados):
    conexao = sqlite3.connect('dados/financas.db')
    cursor = conexao.cursor()
    try:

        cursor.execute("""
            INSERT INTO cotacoes(
            ativo, preco, variacao, data) VALUES (?,?,?,?)
        """, 
        (dados['ativo'],dados['preco'], dados['variacao'], dados['data']))
        conexao.commit()

    except Exception as e:
        logging.error(f'Erro ao salvar os dados na tabela: {e}')
    finally:
        conexao.close()

   
    
def listar_cotacoes():
    conexao = sqlite3.connect('dados/financas.db')
    cursor = conexao.cursor()
    try:
        cursor.execute(f'SELECT * FROM cotacoes')
        linhas = cursor.fetchall()
        return linhas
    except Exception as e:
        logging.error(f'Erro ao buscar cotações: {e}')
    finally:
        conexao.close()