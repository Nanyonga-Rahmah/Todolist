"""Todo controller."""

from Todolist.Backend.models.database_model import db
from Todolist.Backend.models.todo import Todo


class TodoController:
    """A class to connect to the database."""

    def get_todos(self) -> list:
        """Get all todos from the database."""
        todos = db.session.execute(db.select(Todo)).scalars().all()
        return todos
