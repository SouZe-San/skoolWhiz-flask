import pytest

from app import app
from src.database import db_initialize


@pytest.fixture
def client():
    """Setup test client for Flask"""
    app.config["TESTING"] = True
    client = app.test_client()

    # Reinitialize the database for a clean test environment
    db_initialize()

    yield client


def test_create_todo(client):
    """Test creating a new todo item"""
    response = client.post(
        "/todos/", json={"title": "Test Task", "description": "This is a test"})
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Todo created"
    assert "id" in data


def test_get_todos(client):
    """Test retrieving all todo items"""
    # First, create a todo
    client.post(
        "/todos/", json={"title": "Sample Task", "description": "A sample task"})

    response = client.get("/todos/")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0  # At least one todo exists


def test_get_single_todo(client):
    """Test retrieving a single todo item"""
    # First, create a todo
    response = client.post(
        "/todos/", json={"title": "Test Get", "description": "Retrieve test"})
    todo_id = response.get_json()["id"]

    response = client.get(f"/todos/{todo_id}")
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == todo_id
    assert data["title"] == "Test Get"


def test_update_todo(client):
    """Test updating an existing todo item"""
    # First, create a todo
    response = client.post(
        "/todos/", json={"title": "Update Test", "description": "Before update"})
    todo_id = response.get_json()["id"]

    # Update the todo
    response = client.put(
        f"/todos/{todo_id}", json={"title": "Updated Task", "completed": True})
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Todo updated"

    # Verify the update
    response = client.get(f"/todos/{todo_id}")
    data = response.get_json()
    assert data["title"] == "Updated Task"
    assert data["completed"] == True


def test_delete_todo(client):
    """Test deleting a todo item"""
    # First, create a todo
    response = client.post(
        "/todos/", json={"title": "Delete Task", "description": "To be deleted"})
    todo_id = response.get_json()["id"]

    # Delete the todo
    response = client.delete(f"/todos/{todo_id}")
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Todo deleted"

    # Verify deletion
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
