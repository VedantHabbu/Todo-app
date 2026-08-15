# Todo App

A full-stack Todo application built to learn and implement frontend development, REST APIs, database integration, and CRUD operations.

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI
* Pydantic

### Database

* SQLite

### Development Tools

* Git
* GitHub

## Features

* Add new tasks
* Display saved tasks
* Mark tasks as completed
* Unmark completed tasks
* Delete tasks
* Persist tasks using a database
* REST API for Todo operations
* Frontend and backend communication using the Fetch API
* Basic task entry and deletion animations
* Completed task styling
* Data persistence after refreshing or restarting the backend

## Project Structure

```text
todo-app/
├── Backend/
│   ├── main.py
│   ├── database.py
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── .gitignore
```

The local SQLite database file is intentionally excluded from the repository through `.gitignore`.

## API Endpoints

### GET `/todos`

Returns all Todo items stored in the database.

### POST `/todos`

Creates a new Todo item.

Example request:

```json
{
    "task": "Learn FastAPI"
}
```

### PUT `/todos/{id}`

Updates an existing Todo item.

Example request:

```json
{
    "task": "Learn FastAPI",
    "completed": true
}
```

### DELETE `/todos/{id}`

Deletes a Todo item using its ID.

## How It Works

The frontend communicates with the FastAPI backend using JavaScript's Fetch API.

```text
Frontend
    |
    | HTTP requests
    v
FastAPI
    |
    | SQL queries
    v
SQLite
```

The backend handles the REST API endpoints while `database.py` handles database operations.

## Database

The application currently uses SQLite for local persistent storage.

The database contains a `todos` table with the following fields:

```text
id
task
completed
```

SQLite is used in this version to keep the project simple while learning database integration. The database file itself is not committed to GitHub.

## Running Locally

### 1. Start the backend

Navigate to the backend directory:

```bash
cd Backend
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 2. Start the frontend

Open the `Frontend` directory using a local development server such as VS Code Live Server.

The frontend communicates with the FastAPI server running on port 8000.

## Learning Goals

This project was built to understand:

* HTML, CSS, and JavaScript fundamentals
* JavaScript Fetch API
* REST API design
* FastAPI
* Pydantic request models
* HTTP methods
* CRUD operations
* SQLite
* SQL queries
* Database connections and cursors
* Git and GitHub
* Frontend-backend communication
* Basic frontend animations

## Future Improvements

Planned improvements include:

* PostgreSQL database
* Production deployment
* Improved frontend animations
* Better error handling
* Authentication and multi-user functionality in a future project
* React frontend in a future stage of the learning roadmap

## Status

The local full-stack Todo application is complete with working CRUD operations, SQLite persistence, frontend animations, and GitHub version control.

The next planned stage is deployment and migration from SQLite to PostgreSQL.
