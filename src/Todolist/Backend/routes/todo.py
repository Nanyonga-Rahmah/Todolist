"""Todo routes."""

from flask import Blueprint

from Todolist.Backend.controllers.todo import TodoController

todo_routes = Blueprint("todo_routes", __name__)

todo_controller = TodoController()


@todo_routes.route("/todos")
def get_all_todos():
    """Define a route to get all todos."""
    todos = todo_controller.get_todos()
    return todos
