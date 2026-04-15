import sqlite3
import pandas as pd

class GerenciadorDeBanco:
    def __init__(self):
        self.caminho_banco = 'data/data.db'
        self.conexao = sqlite3.connect(self.caminho_banco)
        self.cursor = self.conexao.cursor()
        self._criar_tabela_inicial()

    def _criar_tabela_inicial(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS produtos 
                           (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                           origem TEXT NOT NULL,
                           destino TEXT NOT NULL,
                           produto TEXT NOT NULL,
                           quantidade_energia FLOAT NOT NULL,
                           tipo_fluxo TEXT NOT NULL)''')
        self.conexao.commit()

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
        dataframe.to_sql('produtos', self.conexao, if_exists='replace',index=False)
        

    def remover_registro(self):
        self.cursor.execute('DELETE FROM PRODUTOS;')
        self.cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'produtos';")
        self.conexao.commit()
        