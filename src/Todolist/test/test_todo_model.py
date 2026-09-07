"""Test the Todo model."""

from Todolist.Backend.models.todo import Todo


def test_todo_model() -> None:
    """Test the Todo model."""
    todo = Todo(title="Test Todo", description="This is a test todo item.")
    assert todo.title == "Test Todo"
    assert todo.description == "This is a test todo item."
    assert todo.completed is False
