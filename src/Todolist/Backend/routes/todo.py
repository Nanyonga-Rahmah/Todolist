"""Todo routes."""

from flask import Blueprint, request

from Todolist.Backend.controllers.todo import TodoController

todo_routes = Blueprint("todo_routes", __name__)

todo_controller = TodoController()


@todo_routes.route("/todos")
def get_all_todos():
    """Define a route to get all todos."""
    todos = todo_controller.get_todos()
    return "Todos retrieved successfully", todos


@todo_routes.route("/create-todo", methods=["POST"])
def create_todo():
    """Define a route to create a todo."""
    title = request.form["title"]
    description = request.form["description"]
    created_todo = todo_controller.add_todo(
        {"title": title, "description": description}
    )
    return {"title": created_todo.title, description: created_todo.description}
