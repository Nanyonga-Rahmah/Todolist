"""Todo model."""


class Todo:
    """A class representing a todo item."""

    def __init__(self, title: str, description: str, completed: bool = False):
        """Initialize a new todo item."""
        self.title = title
        self.description = description
        self.completed = completed
