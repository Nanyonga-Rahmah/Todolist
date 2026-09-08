"""Configure test fixtures."""

from collections.abc import Generator

import pytest
from _pytest.assertion import truncate
from faker import Faker
from flask.testing import FlaskClient

from Todolist import create_app
from Todolist.Backend.models.database_model import db

fake = Faker()

# Increase the long string truncation limit when running pytest in
# verbose mode; cf. https://stackoverflow.com/a/60321834.
truncate.DEFAULT_MAX_LINES = 999999
truncate.DEFAULT_MAX_CHARS = 999999


@pytest.fixture
def todo_data() -> dict:
    """Provide sample data for a Todo item."""
    return {
        "id": fake.uuid4(),
        "title": f"{fake.sentence(nb_words=3)}",
        "description": f"{fake.paragraph(nb_sentences=2)}",
        "completed": fake.boolean(),
    }


@pytest.fixture
def setup() -> Generator:
    """Provide a flask app instance with database."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def test_app(setup) -> FlaskClient:
    """Provide a flask testing instannce."""
    return setup.test_client()
