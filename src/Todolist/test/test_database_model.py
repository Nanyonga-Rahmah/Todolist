"""Test database model."""

import pytest
from faker import Faker
from sqlalchemy.exc import IntegrityError

from Todolist.Backend.models.database_model import db
from Todolist.Backend.models.todo import Todo

fake = Faker()


def test_database_model(setup) -> None:
    """Test the database model."""
    assert setup is not None


def test_database_model_gets_all_todos(setup) -> None:
    """Test all todos are retrieved."""
    with setup.app_context():
        todo1 = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        todo2 = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.commit()

        todos = db.session.execute(db.select(Todo)).scalars().all()
        assert len(todos) == 2


def test_database_model_add_todo(setup) -> None:
    """Test a todo is added to the database."""
    with setup.app_context():
        todo = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo)
        db.session.commit()

        retrieved_todo = db.session.execute(
            db.select(Todo).filter_by(id=todo.id)
        ).scalar_one_or_none()
        assert retrieved_todo is not None
        assert retrieved_todo.title == todo.title
        assert retrieved_todo.description == todo.description
        assert retrieved_todo.completed == todo.completed


def test_database_model_delete_todo(setup) -> None:
    """Test a todo is deleted from the database."""
    with setup.app_context():
        todo = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo)
        db.session.commit()

        db.session.delete(todo)
        db.session.commit()

        retrieved_todo = db.session.execute(
            db.select(Todo).filter_by(id=todo.id)
        ).scalar_one_or_none()
        assert retrieved_todo is None


def test_database_model_update_todo(setup) -> None:
    """Test a todo can be updated in the database."""
    with setup.app_context():
        todo = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo)
        db.session.commit()
        todo.title = f"{fake.sentence(nb_words=5)}"

        db.session.commit()
        retrieved_todo = db.session.execute(
            db.select(Todo).filter_by(id=todo.id)
        ).scalar_one_or_none()
        assert retrieved_todo.title == todo.title


def test_todos_have_unqiue_ids(setup) -> None:
    """Test that todos have unique IDs."""
    with setup.app_context():
        todo1 = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        todo2 = Todo(
            title=fake.sentence(nb_words=3),
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo1)
        db.session.add(todo2)
        db.session.commit()

        assert todo1.id != todo2.id


def test_database_rejects_todos_without_title(setup) -> None:
    """Test that todos without a title are rejected."""
    with setup.app_context():
        todo = Todo(
            title=None,
            id=fake.uuid4(),
            description=fake.paragraph(nb_sentences=2),
            completed=fake.boolean(),
        )
        db.session.add(todo)
        with pytest.raises(IntegrityError):
            db.session.commit()
