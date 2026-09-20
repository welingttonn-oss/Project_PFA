import sqlite3
import logging

# Função de criar tabelas, caso já existe o IF NOT Exists ele ignora a função.
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

        
        logging.info('Tabela cotacoes pronta (verificada).')

    except sqlite3.ProgrammingError as e: #erro no código SQL (ex.: comando mal escrito).
        logging.error(f'Erro no código: {e}')
    except sqlite3.DatabaseError as e: # erro no banco em si (ex.: arquivo corrompido).
        logging.error(f'Erro no Bancos: {e}')
    except Exception as e:
        logging.error(f'Erro na criação da Tabela: {e}')
    finally:
        cursor.close()
        conexao.close()

#Função de salvar os ativos na tabela criada. receberá o dicionário da função obter_dados(src/coleta.py) acionado no main.py

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

    except sqlite3.OperationalError as e: # tabela inexistente, banco travado.
        logging.error(f'SQL errado, tabela inexistente: {e}')    
    except sqlite3.IntegrityError as e: # violação de regra (ex.: NOT NULL violado).
        logging.error(f'Violação de regra: {e}')
    except Exception as e:
        logging.error(f"Erro ao salvar {dados['ativo']}: {e}")
    finally:
        cursor.close()
        conexao.close()


 #Função de listar cotações criadas anteriormente, ainda não está sendo usada no main.py  
    
def listar_cotacoes():
    conexao = sqlite3.connect('dados/financas.db')
    cursor = conexao.cursor()
    try:
        cursor.execute('SELECT * FROM cotacoes')
        linhas = cursor.fetchall()
        return linhas
    except sqlite3.OperationalError as e: # tabela inexistente, banco travado.
        logging.error(f'SQL errado, tabela inexistente: {e}')  
    
    except Exception as e:
        logging.error(f'Erro ao buscar cotações: {e}')
    finally:
        cursor.close()
        conexao.close()