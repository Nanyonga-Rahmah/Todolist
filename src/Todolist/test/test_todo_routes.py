"""Test Todo Routes."""


def test_todo_retrieval(test_app) -> None:
    """Test route for retrieving todos."""
    response = test_app.get("/todos")
    assert response.status_code == 200
