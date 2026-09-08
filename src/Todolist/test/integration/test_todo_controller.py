"""Test todo controller."""

from Todolist.Backend.controllers.todo import TodoController


def test_todo_controller_get_todos(setup) -> None:
    """Test the get_todos function."""
    with setup.app_context():
        controller = TodoController()
        todos = controller.get_todos()
        assert isinstance(todos, list)
