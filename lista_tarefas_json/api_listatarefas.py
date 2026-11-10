import json

from flask import Flask, request

app = Flask(__name__)
with open("tarefas.json", "r", encoding="utf-8") as f:
    tarefas = json.load(f)

def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

@app.route("/")
def home():
    return "API de Lista de Tarefas"

@app.route("/tarefas")
def listar_tarefas():
    return tarefas

@app.route("/adicionar")
def adicionar():
    titulo = request.args.get("titulo")
    
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    }
    
    tarefas.append(nova_tarefa)
    
    salvar_tarefas()
    
    return nova_tarefa

@app.route("/remover/<int:id>")
def remover(id):
    
    for tarefa in tarefas:
        
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            salvar_tarefas()
            
            return {
                "mensagem": f"tarefa {id} removida com sucesso!"
            }
            
    return {
        "erro": "Tarefa não encontrada"
    }
    
@app.route("/concluir/<int:id>")
def concluir(id):
    
    for tarefa in tarefas:
        
        if tarefa["id"] == id:
            
            tarefa["concluida"] = True
            
            salvar_tarefas()
            
            return {
                "mensagem": f"Tarefa {id} concluída!"
                
            }    
    return {
        "erro": "Tarefa não encontrada"
    }
    
@app.route("/editar/<int:id>")
def editar(id):
    
    novo_titulo = request.args.get("titulo")
    
    for tarefa in tarefas:
        
        if tarefa["id"] == id:
            
            tarefa["titulo"] = novo_titulo
            
            salvar_tarefas()
            
            return {
                "mensagem": f"Tarefa {id} editada com sucesso!"
            }
    return {
        "erro": "Tarefa não encontrada"
    }
app.run()