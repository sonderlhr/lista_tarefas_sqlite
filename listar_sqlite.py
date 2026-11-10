import sqlite3

conexao = sqlite3.connect("tarefas.db")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM tarefas")

tarefas = cursor.fetchall()

for tarefa in tarefas:
    print(tarefa)
    
conexao.close()