"""Todo model."""


class Todo:
    """A class representing a todo item."""

    def __init__(self, title: str, id: int, description: str, completed: bool = False):
        """Initialize a new todo item."""
        self.title = title
        self.id = id
        self.description = description
        self.completed = completed
