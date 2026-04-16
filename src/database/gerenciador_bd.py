import sqlite3
import pandas as pd

class GerenciadorDeBanco:
    def __init__(self):
        self.caminho_banco = 'data/data.db'

    def _conectar_banco(self):
        return sqlite3.connect(self.caminho_banco)

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
            dataframe.to_sql('produtos', conexao, if_exists='append',index=False)
        
    def remover_registros(self):
        with self._conectar_banco() as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM PRODUTOS;')
            cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'produtos';")

    def select_query(self, nome_do_produto):
        with self._conectar_banco() as conexao:
            df = pd.read_sql_query('SELECT * FROM produtos WHERE produto = ?', con=conexao, params=(nome_do_produto,))
            return df
        
gerenciador = GerenciadorDeBanco()