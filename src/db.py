import sqlite3
import logging

# Função de criar tabelas, caso já existe o IF NOT Exists ele ignora a função.
def criar_tabela():

    """
    Cria a tabela de cotações no banco SQLite.

    Não recebe parâmetros. Se a tabela já existir, não faz nada
    (graças ao IF NOT EXISTS). Colunas criadas:

        - id: identificador único (auto-incremento).
        - ativo: código do ativo (ex.: USD-BRL, PETR4.SA).
        - preco: valor do ativo no momento da coleta.
        - variacao: variação em relação ao fechamento anterior (pode ser None).
        - data: data e hora da coleta no formato "YYYY-MM-DD HH:MM:SS".

    Parâmetros:
        Nenhum.

    Retorno:
        Nenhum (função de ação — apenas cria a tabela).
    """

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
        logging.error(f'Erro no Banco: {e}')
    except Exception as e:
        logging.error(f'Erro na criação da Tabela: {e}')
    finally:
        cursor.close()
        conexao.close()

#Função de salvar os ativos na tabela criada. receberá o dicionário da função obter_dados(src/coleta.py) acionado no main.py

def salvar_cotacao(dados):

    """
    Salva uma cotação na tabela `cotacoes` do banco.

    Recebe o dicionário retornado por `obter_dados()` e o insere
    no banco. Cada chamada adiciona uma nova linha (não sobrescreve).

    Parâmetros:
        dados (dict): dicionário com as chaves:
            - ativo: código do ativo (ex.: USD-BRL, PETR4.SA).
            - preco: valor do ativo no momento da coleta.
            - variacao: variação em relação ao fechamento anterior (pode ser None).
            - data: data e hora da coleta.

    Retorno:
        Nenhum (função de ação — apenas salva no banco).
    """
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


 #Função que lista todas as cotações salvas no banco 
    
def listar_cotacoes():
    """
    Lista todas as cotações do banco.

    Parâmetros:
        Nenhum.

    Retorno:
        list: lista de tuplas, cada uma representando uma linha
        da tabela `cotacoes` no formato (id, ativo, preco, variacao, data).
    """
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

# função para ordenar e trazer uma quantidade limitada para o LOG.
def listar_ultimas(limite):

    if limite > 0: # valida se a solicitação é maior que zero, caso sim executa
        conexao = sqlite3.connect('dados/financas.db')
        cursor = conexao.cursor()
        try:
            cursor.execute('''
                SELECT *
                FROM cotacoes
                ORDER BY id DESC
                LIMIT ?
            ''', (limite,))

            linhas = cursor.fetchall()
            return linhas
        except sqlite3.OperationalError as e:
            logging.error(f'erro de tabela inexistente, banco travado: {e}')
        except Exception as e:
            logging.error(f'Erro ao buscar cotações: {e}')
        finally:
            cursor.close()
            conexao.close()
    else:
        logging.warning(f'Não é possivel executar limite negativo: {limite}')
        return None
 