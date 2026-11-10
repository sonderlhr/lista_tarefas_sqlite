import sqlite3

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM tarefas")
    
    tarefas = cursor.fetchall()
    
    conexao.close()
    
    return render_template(
        "index.html",
        tarefas=tarefas
    )


@app.route("/tarefas")
def listar_tarefas():
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM tarefas")
    
    tarefas_banco = cursor.fetchall()
    
    conexao.close()
    
    tarefas = []
    
    for tarefa in tarefas_banco:
        
        tarefas.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2]),
            "prioridade": tarefa[3],
            "data_limite": tarefa[4]
            
        })
    
    return tarefas    

@app.route("/adicionar")
def adicionar():

    titulo = request.args.get("titulo")
    prioridade = request.args.get("prioridade")
    data_limite = request.args.get("data_limite")


    conexao = sqlite3.connect("tarefas.db")

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO tarefas
        (titulo, concluida, prioridade, data_limite)
        VALUES (?, ?, ?, ?)
        """,
        (titulo, 0, prioridade, data_limite)
    )

    conexao.commit()

    conexao.close()
    
    return redirect("/")

    return {
        "mensagem": "Tarefa adicionada com sucesso!"
    }
    
@app.route("/remover/<int:id>")
def remover(id):
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    )
    
    tarefa = cursor.fetchone()
    
    if tarefa is None:
        
        conexao.close()
        
        return {
            "erro": "Tarefa não encontrada"
        }
        
    cursor.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )
    
    conexao.commit()
    
    conexao.close()
    
    return redirect("/")
    
@app.route("/concluir/<int:id>")
def concluir(id):
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id,)
        
    )
    conexao.commit()
    
    conexao.close()
    
    return redirect("/")

@app.route("/pendentes")
def pendentes():
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT * FROM tarefas WHERE concluida = 0"
    )
    
    tarefas_banco = cursor.fetchall()
    
    conexao.close()
    
    tarefas = []
    
    for tarefa in tarefas_banco:
        
        tarefas.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2]),
            "prioridade": tarefa[3],
            "data_limite": tarefa[4]
        })

    return tarefas 

@app.route("/concluidas")
def concluidas():
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT * FROM tarefas WHERE concluida = 1"
        
    )

    tarefas_banco = cursor.fetchall()
    
    conexao.close()
    
    tarefas = []
    
    for tarefa in tarefas_banco:
        
        tarefas.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2])
            
        })
        
    return tarefas


@app.route("/buscar")
def buscar():
    
    titulo = request.args.get("titulo")
    
    conexao = sqlite3.connect("tarefas.db")
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "SELECT * FROM tarefas WHERE titulo LIKE?",
        (f"%{titulo}%",)
    )

    tarefas_banco = cursor.fetchall()
    
    conexao.close()
    
    tarefas = []
    
    for tarefa in tarefas_banco:
        
        tarefas.append({
            "id": tarefa[0],
            "titulo": tarefa[1],
            "concluida": bool(tarefa[2])
        })
        
    return tarefas

@app.route("/editar/<int:id>")
def editar(id):
    
    novo_titulo = request.args.get("titulo")
    
    conexao = sqlite3.connect("tarefas.db")
    
    
    cursor = conexao.cursor()
    
    cursor.execute(
        "UPDATE tarefas SET titulo = ? WHERE id = ?",
        (novo_titulo, id)
    )
    
    conexao.commit()
    
    conexao.close()
    
    return redirect("/")


app.run()
