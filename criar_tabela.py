import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas(
    id INTEGER PRIMARY KEY,
    titulo TEXT, 
    concluida BOOLEAN,
    prioridade TEXT,
    data_limite TEXT
)
""")

conexao.commit()

conexao.close()

print("Tabela criada com sucesso!")