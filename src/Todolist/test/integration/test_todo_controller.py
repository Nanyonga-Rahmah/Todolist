"""Test todo controller."""

from faker import Faker

from Todolist.Backend.controllers.todo import TodoController

fake = Faker()


def test_todo_controller_get_todos(setup) -> None:
    """Test the get_todos function."""
    with setup.app_context():
        controller = TodoController()
        todos = controller.get_todos()
        assert isinstance(todos, list)


def test_todo_controller_adds_a_todo(setup, todo_data) -> None:
    """Test the add_todo function."""
    with setup.app_context():
        controller = TodoController()
        todo = controller.add_todo(todo_data)
        assert todo.id == todo_data["id"]
        assert todo.title == todo_data["title"]
        assert todo.description == todo_data["description"]
        assert todo.completed == todo_data["completed"]


def test_todo_controller_deletes_a_todo(setup, todo_data) -> None:
    """Test the delete_todo function."""
    with setup.app_context():
        controller = TodoController()
        todo = controller.add_todo(todo_data)
        removed_todo = controller.delete_todo(todo.id)
        assert removed_todo.id == todo.id


def test_todo_controller_updates_a_todo(setup, todo_data) -> None:
    """Test the update_todo function."""
    with setup.app_context():
        controller = TodoController()
        todo = controller.add_todo(todo_data)
        todo.title = f"{fake.sentence(nb_words=5)}"
        todo.description = f"{fake.paragraph(nb_sentences=3)}"
        todo.completed = fake.boolean()

        updated_todo = controller.update_todo(
            todo.id,
            {
                "title": todo.title,
                "description": todo.description,
                "completed": todo.completed,
            },
        )
        assert updated_todo.title == todo.title
        assert updated_todo.description == todo.description
        assert updated_todo.completed == todo.completed
