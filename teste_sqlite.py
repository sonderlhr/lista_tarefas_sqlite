import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("PRAGMA table_info(tarefas)")
                      
print(cursor.fetchall())

conexao.close()