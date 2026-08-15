import os
import psycopg

def get_connection():
    return psycopg.connect(os.getenv("DATABASE_URL"))

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_todo(task, completed):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todos (task, completed) VALUES (%s, %s) RETURNING id",
        (task, completed)
    )

    conn.commit()

    todo_id = cursor.fetchone()[0]

    conn.close()

    return todo_id

def get_todos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM todos")

    rows = cursor.fetchall()

    todos = []

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
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE todos SET task = %s, completed = %s WHERE id = %s",
        (task,completed,id)
        )

    conn.commit()
    conn.close()

def delete_todo(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM todos WHERE id = %s",
        (id,)
    )

    conn.commit()
    conn.close()