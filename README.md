# Todo App

A full-stack Todo application built from scratch using vanilla JavaScript, FastAPI, and PostgreSQL. The application is deployed publicly using Vercel and Railway.

## Live Demo

Frontend:
https://todo-app-indol-iota-18.vercel.app

Backend API:
https://todo-app-production-9014.up.railway.app

### Backend Routes

- GET `/todos`
- POST `/todos`
- PUT `/todos/{id}`
- DELETE `/todos/{id}`

API Documentation:
https://todo-app-production-9014.up.railway.app/docs

---

## Features

- Add new Todo tasks
- View saved Todo tasks
- Mark tasks as completed or uncompleted
- Delete Todo tasks
- Persistent cloud database storage
- REST API built with FastAPI
- PostgreSQL database
- Responsive frontend
- Public deployment

Task text editing is planned for v1.1.

---

## Tech Stack

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### Database

- PostgreSQL
- Psycopg 3

### Deployment

- Vercel — Frontend
- Railway — FastAPI Backend
- Railway PostgreSQL — Database

### Version Control

- Git
- GitHub

---

## Architecture

```text
                    User
                     |
                     v
              +-------------+
              |   Vercel    |
              |  Frontend   |
              | HTML/CSS/JS |
              +------+------+
                     |
                  HTTP API
                     |
                     v
              +-------------+
              |   Railway   |
              |   FastAPI   |
              |   Backend   |
              +------+------+
                     |
               DATABASE_URL
                     |
                     v
              +-------------+
              |   Railway   |
              | PostgreSQL  |
              +-------------+
