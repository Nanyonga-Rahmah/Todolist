const button = document.getElementById("button")
const form = document.getElementById("form")
const cancelButton = document.getElementById("cancel")
const titleElement = document.getElementById("title")
const descriptionElement = document.getElementById("description")
const todoList = document.getElementById("todos");

let title;
let description;



button.addEventListener("click", () => {
    form.classList.add("view-form")
})

cancelButton.addEventListener("click", () => {
    form.classList.remove("view-form")

})



form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    try {
        const response = await fetch("http://localhost:5000/create-todo", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            console.error("Failed to create todo:", data);
            return;
        }


        form.reset();
        form.classList.remove("view-form");

    } catch (error) {
        console.error("Request failed:", error);
    }
});



const displayTodos = async () => {
    try {
        const response = await fetch("http://localhost:5000/todos");

        const data = await response.json();

        if (!response.ok) {
            console.error("Failed to retrieve todos:", data);
            return;
        }

        todoList.innerHTML = "";

        data.todos.forEach((todo) => {
            const todoElement = document.createElement("div");

            todoElement.classList.add("todo");

            todoElement.innerHTML = `
            <input type="checkbox" id=${todo.id} name=${todo.title} value=${todo.title}>
                <h3>${todo.title}</h3>
            `;

            todoList.appendChild(todoElement);
        });

    } catch (error) {
        console.error("Failed to retrieve todos:", error);
    }
};

displayTodos();
