"""Test the Todo model."""

from Todolist.Backend.models.todo import Todo


def test_todo_model(todo_data: dict) -> None:
    """Test the Todo model."""
    todo = Todo(**todo_data)
    assert todo.id == todo_data["id"]
    assert todo.title == todo_data["title"]
    assert todo.description == todo_data["description"]
    assert todo.completed == todo_data["completed"]


def test_todo_model_default_completed(todo_data: dict) -> None:
    """Test the Todo model is not completed by default."""
    todo_data.pop("completed")
    todo = Todo(**todo_data)
    assert todo.completed is False
