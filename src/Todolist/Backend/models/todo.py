"""Todo model."""

from Todolist.Backend.models.database_model import db


class Todo(db.Model):
    """A class representing a todo item."""

    id = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, title: str, id: str, description: str, completed: bool = False):
        """Initialize a new todo item."""
        self.title = title
        self.id = id
        self.description = description
        self.completed = completed
