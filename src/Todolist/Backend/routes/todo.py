"""Todo routes."""

from flask import Blueprint, request

from Todolist.Backend.controllers.todo import TodoController

todo_routes = Blueprint("todo_routes", __name__)

todo_controller = TodoController()


@todo_routes.route("/todos")
def get_all_todos() -> dict[str, dict]:
    """Define a route to get all todos."""
    todos = todo_controller.get_todos()
    return {"message": "Todos retrieved successfully", "todos": todos}


@todo_routes.route("/create-todo", methods=["POST"])
def create_todo() -> dict[str, str]:
    """Define a route to create a todo."""
    title = request.form["title"]
    description = request.form["description"]
    created_todo = todo_controller.add_todo(
        {"title": title, "description": description}
    )
    return {"title": created_todo.title, "description": created_todo.description}


@todo_routes.route("/update-todo/<int:id>", methods=["PATCH"])
def update_todo(id: int) -> str:
    """Define a route for updating a todo."""
    if id is None:
        return "Missing todo-id", 404
    else:
        title = request.form["title"]
        description = request.form["description"]
        completed = request.form["completed"]
        updated_todo = todo_controller.update_todo(
            todo_id=id,
            updated_data={
                "title": title,
                "description": description,
                "completed": completed,
            },
        )
    return "Todo updated successfuly", updated_todo


@todo_routes.route("/delete-todo/<int:id>", methods=["DELETE"])
def delete_todo(id: int) -> tuple[dict, int]:
    """Define route for deleting a todo."""
    if id is None:
        return "Missing todo-id", 404
    else:
        deleted_todo = todo_controller.delete_todo(todo_id=id)
    return {
        "message": "Todo deleted successfully",
        "todo": {
            "id": deleted_todo.id,
            "title": deleted_todo.title,
            "description": deleted_todo.description,
            "completed": deleted_todo.completed,
        },
    }, 200
