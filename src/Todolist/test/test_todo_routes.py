"""Test Todo Routes."""

from flask.testing import FlaskClient


def test_todo_retrieval(test_app) -> None:
    """Test route for retrieving todos."""
    response = test_app.get("/todos")
    assert response.status_code == 200
    assert b"Todos" in response.data


def test_todo_retrieval_rejects_a_post(test_app: FlaskClient) -> None:
    """Test retriving todos with a post."""
    response = test_app.post("/todos")
    assert response.status_code == 405


def test_todo_creation(test_app: FlaskClient, todo_data) -> None:
    """Test route for creating a todo."""
    response = test_app.post("/create-todo", data=(todo_data))
    assert response.status_code == 200
    assert b"title" in response.data
