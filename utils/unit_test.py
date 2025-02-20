import unittest
import sqlite3
import json
from app import app
from src.database import create_connection, db_initialize


class TodoAPITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize database once for all tests."""
        db_initialize()

    def setUp(self):
        """Set up a test client and reset the database before each test."""
        self.app = app.test_client()
        self.app.testing = True

        # Clear the database before each test
        conn, cursor = create_connection()
        cursor.execute("DELETE FROM todos")
        conn.commit()
        conn.close()

    def test_create_todo(self):
        """Test creating a new Todo item."""
        response = self.app.post("/todos",
                                 data=json.dumps(
                                     {"title": "Test Todo", "description": "Test Desc"}),
                                 content_type="application/json")

        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertIn("Todo created", data["message"])

    def test_get_todos(self):
        """Test retrieving all todos."""
        # Insert a test todo
        conn, cursor = create_connection()
        cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)",
                       ("Sample Todo", "Sample Desc"))
        conn.commit()
        conn.close()

        response = self.app.get("/todos")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Sample Todo")

    def test_get_single_todo(self):
        """Test retrieving a single todo item."""
        conn, cursor = create_connection()
        cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)",
                       ("Single Todo", "Description"))
        todo_id = cursor.lastrowid
        conn.commit()
        conn.close()

        response = self.app.get(f"/todos/{todo_id}")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["title"], "Single Todo")

    def test_update_todo(self):
        """Test updating a todo item."""
        conn, cursor = create_connection()
        cursor.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)", ("Old Title", "Old Desc"))
        todo_id = cursor.lastrowid
        conn.commit()
        conn.close()

        update_data = {"title": "Updated Title", "completed": 1}
        response = self.app.put(f"/todos/{todo_id}",
                                data=json.dumps(update_data),
                                content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Todo updated", response.get_json()["message"])

    def test_delete_todo(self):
        """Test deleting a todo item."""
        conn, cursor = create_connection()
        cursor.execute(
            "INSERT INTO todos (title, description) VALUES (?, ?)", ("To be deleted", "Desc"))
        todo_id = cursor.lastrowid
        conn.commit()
        conn.close()

        response = self.app.delete(f"/todos/{todo_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Todo deleted", response.get_json()["message"])

    def test_invalid_todo_fetch(self):
        """Test retrieving a non-existent todo item."""
        response = self.app.get("/todos/9999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("Todo not found", response.get_json()["error"])


if __name__ == "__main__":
    unittest.main()
