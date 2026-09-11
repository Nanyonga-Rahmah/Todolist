"""Todo controller."""

from Todolist.Backend.models.database_model import db
from Todolist.Backend.models.todo import Todo


class TodoController:
    """A class to connect to the database."""

    def get_todos(self) -> list:
        """Get all todos from the database."""
        todos = db.session.execute(db.select(Todo)).scalars().all()
        return todos

    def add_todo(self, todo_data: dict) -> Todo:
        """Add a new todo to the database."""
        todo = Todo(**todo_data)
        db.session.add(todo)
        db.session.commit()
        return todo

    def delete_todo(self, todo_id: str) -> Todo:
        """Delete a todo from the database."""
        todo = db.session.execute(
            db.select(Todo).filter_by(id=todo_id)
        ).scalar_one_or_none()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return todo

    def update_todo(self, todo_id: str, updated_data: Todo) -> Todo:
        """Update a todo in the database."""
        retrieved_todo = db.session.execute(
            db.select(Todo).filter_by(id=todo_id)
        ).scalar_one_or_none()
        if retrieved_todo:
            retrieved_todo.title = updated_data["title"]
            retrieved_todo.description = updated_data["description"]
            retrieved_todo.completed = updated_data["completed"]
            db.session.commit()
        return retrieved_todo
