import sqlite3

def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_todo(task, completed):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todos (task, completed) VALUES (?, ?)",
        (task, completed)
    )

    conn.commit()

    todo_id = cursor.lastrowid

    conn.close()

    return todo_id

def get_todos():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos")

    rows = cursor.fetchall()

    todos=[]

    for row in rows:
        todo={
            "id":row[0],
            "task":row[1],
            "completed":bool(row[2])
        }
        todos.append(todo)

    conn.close()

    return todos

def update_todo(task, completed, id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE todos SET task = ?, completed = ? WHERE id = ?",
        (task,completed,id)
        )

    conn.commit()
    conn.close()

def delete_todo(id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM todos WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()
