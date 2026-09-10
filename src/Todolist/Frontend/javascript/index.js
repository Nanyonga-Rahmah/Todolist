const button = document.getElementById("button")
const form = document.getElementById("form")
const cancelButton = document.getElementById("cancel")
const titleElement = document.getElementById("title")
const descriptionElement = document.getElementById("description")
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
