"""Project metadata."""

from flask import Flask

from Todolist.Backend.models.database_model import db


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    db.init_app(app)

    return app
