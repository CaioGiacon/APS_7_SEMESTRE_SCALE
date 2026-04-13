import sqlite3
import pandas as pd

df = pd.read_csv('dataset_etanol_toy.csv')
# Conectando ao banco de dados
conexao = sqlite3.connect('data/data.db')

# Criando o cursor para executar comandos SQL
cursor = conexao.cursor()

#Criando as tabelas
#cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,origem TEXT NOT NULL,destino TEXT NOT NULL,produto TEXT NOT NULL,quantidade_energia FLOAT NOT NULL,tipo_fluxo TEXT NOT NULL)''')

df.to_sql('produtos', conexao,
          if_exists='replace',
          index=False)

# Commit nos comandos
#conexao.commit()

# Fechando a conexão
conexao.close()