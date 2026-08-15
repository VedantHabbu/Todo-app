from database import (
    init_db,
    add_todo,
    get_todos as get_todos_db,
    update_todo as update_todo_db,
    delete_todo as delete_todo_db
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://todo-app-indol-iota-18.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
def get_todos():
    todos = get_todos_db()
    return todos

class TodoCreate(BaseModel):
    task: str

class TodoUpdate(BaseModel):
    task: str
    completed: bool

@app.post("/todos")
def create_todo(todo: TodoCreate):
    todo_id = add_todo(todo.task,False)
    return {
        "id": todo_id,
        "task": todo.task,
        "completed": False
    }

@app.delete("/todos/{id}")
def delete_todo(id: int):
    delete_todo_db(id)

    return{
        "message": "Todo Deleted"
    }

@app.put("/todos/{id}")
def update_todo(id: int, todo: TodoUpdate):
    update_todo_db(todo.task,todo.completed,id)

    return {
        "id": id,
        "task": todo.task,
        "completed": todo.completed
    }






    