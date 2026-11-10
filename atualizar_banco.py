import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("""
ALTER TABLE tarefas
ADD COLUMN prioridade TEXT
""")

cursor.execute("""
ALTER TABLE tarefas
ADD COLUMN data_limite TEXT 
""")

conexao.commit()

conexao.close()

print("Banco atualizado!")