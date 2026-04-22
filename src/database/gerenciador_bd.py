import sqlite3
import pandas as pd

class GerenciadorDeBanco:
    def __init__(self):
        self.caminho_banco = 'data/data.db'

    def _conectar_banco(self):
        return sqlite3.connect(self.caminho_banco)
    
    def criar_tabela(self):
        with self._conectar_banco() as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS produtos(
                           id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                           origem TEXT NOT NULL,
                           destino TEXT NOT NULL,
                           produto TEXT NOT NULL,
                           quantidade INTEGER NOT NULL,
                           tipo_fluxo TEXT NOT NULL,
                           transformidade TEXT NOT NULL);''')

    def ler_arquivo_do_usuario(self, arquivo):
        try:
            df = pd.read_csv(arquivo, sep=',', encoding='utf-8')
            return df
        except PermissionError:
            print('Você não tem permissão para ler este arquivo')
        except pd.errors.ParserError:
            print('Erro: Estrutura do CSV inválida.')
        except UnicodeDecodeError:
            df = pd.read_csv(arquivo, sep=',', encoding='ISO-8859-1')
        except FileNotFoundError:
            print('Erro: Arquivo não encontrado')
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')
    
    def enviar_registros_para_sqlite(self, dataframe):
        with self._conectar_banco() as conexao:  
            dataframe.to_sql('produtos', conexao, if_exists='replace',index=False)
                
    def select_query(self, nome_do_produto):
        with self._conectar_banco() as conexao:
            df = pd.read_sql_query('''
                                   WITH RECURSIVE grafo AS (
                                        SELECT * FROM produtos WHERE produto = ?
                                        UNION ALL
                                        
                                        SELECT p.* FROM produtos p 
                                        INNER JOIN grafo g ON p.destino = g.origem
                                   )
                                   SELECT * FROM grafo;
                                ''', con=conexao, params=(nome_do_produto,))
            return df
        
gerenciador = GerenciadorDeBanco()