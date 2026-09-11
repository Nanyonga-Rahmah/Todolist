"""Test Todo Routes."""

from faker import Faker
from flask.testing import FlaskClient

from Todolist.Backend.models.todo import Todo

fake = Faker()


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


def test_updating_a_todo(test_app: FlaskClient, todo_data: Todo) -> None:
    """Test route for updating a todo."""
    response = test_app.patch("/update-todo/1", data=(todo_data))
    assert response.status_code == 200
    assert b"Todo updated" in response.data


def test_updating_todo_allows_patch_requests(test_app: FlaskClient, todo_data) -> None:
    """Test that the update route allows patch requests."""
    response = test_app.post("/update-todo/1", data=(todo_data))
    assert response.status_code == 405


def test_update_route_receives_a_todo_id(
    test_app: FlaskClient, todo_data: Todo
) -> None:
    """Test the update route expects a todo_id."""
    response = test_app.patch("/update-todo/1", data=todo_data)
    assert response.status_code == 200


def test_update_route_missing_a_todo_id(test_app: FlaskClient, todo_data: Todo) -> None:
    """Test that the update route expects todo-id."""
    response = test_app.patch("/update-todo", data=todo_data)
    assert response.status_code == 404


def test_deleting_a_todo(test_app: FlaskClient, stored_todo: Todo) -> None:
    """Test route for deleting a todo."""
    response = test_app.delete(f"/delete-todo/{stored_todo.id}")
    assert response.status_code == 200
    assert b"Todo deleted" in response.data
    assert b"title" in response.data
