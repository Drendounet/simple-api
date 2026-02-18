from fastapi import FastAPI, HTTPException
from app.models import Todo, TodoCreate
from typing import List

app = FastAPI(
    title="Simple Todo API",
    description="Une API REST simple pour gérer des todos",
    version="1.0.0"
)

# Base de données en mémoire (pour commencer)
todos_db: List[Todo] = []
todo_id_counter = 1

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Todo! Visitez /docs pour la documentation"}

@app.get("/todos", response_model=List[Todo])
def get_todos():
    """Récupère tous les todos"""
    return todos_db

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """Récupère un todo spécifique"""
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo non trouvé")

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    """Crée un nouveau todo"""
    global todo_id_counter
    new_todo = Todo(
        id=todo_id_counter,
        title=todo.title,
        description=todo.description,
        completed=False
    )
    todos_db.append(new_todo)
    todo_id_counter += 1
    return new_todo

@app.patch("/todos/{todo_id}/complete", response_model=Todo)
def complete_todo(todo_id: int):
    """Marque un todo comme complété"""
    for todo in todos_db:
        if todo.id == todo_id:
            todo.completed = True
            return todo
    raise HTTPException(status_code=404, detail="Todo non trouvé")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    """Supprime un todo"""
    global todos_db
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Todo non trouvé")
