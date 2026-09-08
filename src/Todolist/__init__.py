"""Project metadata."""

from flask import Flask

from Todolist.Backend.models.database_model import db
from Todolist.Backend.routes.todo import todo_routes


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)
    app.register_blueprint(todo_routes)

    return app
