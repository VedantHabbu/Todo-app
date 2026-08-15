const addButton = document.getElementById("add-btn");
const taskInput = document.getElementById("task-input");
const taskContainer = document.getElementById("task-container");
const API_URL = "https://todo-app-production-9014.up.railway.app";

let tasks = [];

fetch(`${API_URL}/todos`)
    .then(response => response.json())
    .then(data => {
        tasks = data;

        data.forEach(function(todo){
            addTask(todo);
        });
    });

addButton.addEventListener("click", function() {
    const task = taskInput.value.trim();

    if (task === "") {
        alert("Please enter a task!!");
        return;
    }

    fetch(`${API_URL}/todos`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            task: task
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        tasks.push(data);
        addTask(data);
    });
});

taskInput.addEventListener("keydown", function(event){
    if(event.key === "Enter"){
        addButton.click();
    }
});

function addTask(todo){

    const newTask = document.createElement("div");
    const taskText = document.createElement("span");
    const completedButton = document.createElement("button");
    const removeButton = document.createElement("button");
    removeButton.style.backgroundColor = "red";
    
    taskText.textContent = todo.task;
    completedButton.textContent = "✔";
    removeButton.textContent = "🗑";

    if (todo.completed === true) {
        completedButton.style.backgroundColor = "green";
        taskText.style.textDecoration = "line-through";
        taskText.classList.add("completed-text");
    }

    newTask.appendChild(taskText);
    newTask.appendChild(completedButton);
    newTask.appendChild(removeButton);
    
    taskContainer.appendChild(newTask);
    taskInput.value = "";

    removeButton.addEventListener("click", function(){
        fetch(`${API_URL}/todos/${todo.id}`, {
            method: "DELETE"
        })
        .then(() => {
            newTask.classList.add("removing");

            setTimeout(() => {
                newTask.remove();
            }, 300);
        });
    });

    completedButton.addEventListener("click", function() {

        if (completedButton.style.backgroundColor === "green") {

            completedButton.style.backgroundColor = "";
            taskText.style.textDecoration = "none";
            taskText.classList.remove("completed-text");

            fetch(`${API_URL}/todos/${todo.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    task: todo.task,
                    completed: false
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            });

        } else {

            completedButton.style.backgroundColor = "green";
            taskText.style.textDecoration = "line-through";
            taskText.classList.add("completed-text");

            fetch(`${API_URL}/todos/${todo.id}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    task: todo.task,
                    completed: true
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            });
        }

    });
}