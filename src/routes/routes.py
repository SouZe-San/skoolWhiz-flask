from flask import request, jsonify
from flask_restful import Resource
import sqlite3
from src.database import create_connection


class TodoListResource(Resource):
    def get(self):
        """Retrieve all todos"""
        conn, cursor = create_connection()
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        conn.close()

        return jsonify([
            {"id": row["id"], "title": row["title"],
                "description": row["description"], "completed": bool(row["completed"])}
            for row in todos
        ])

    def post(self):
        """Create a new todo"""
        data = request.get_json()
        if "title" not in data:
            return {"error": "Title is required"}, 400

        conn, cursor = create_connection()
        cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)",
                       (data["title"], data.get("description", "")))
        conn.commit()
        todo_id = cursor.lastrowid
        conn.close()

        return {"message": "Todo created", "id": todo_id}, 201


class TodoResource(Resource):
    def get(self, todo_id):
        """Retrieve a single todo"""
        conn, cursor = create_connection()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
        todo = cursor.fetchone()
        conn.close()

        if not todo:
            return {"error": "Todo not found"}, 404

        return {"id": todo["id"], "title": todo["title"], "description": todo["description"], "completed": bool(todo["completed"])}

    def put(self, todo_id):
        """Update a todo"""
        data = request.get_json()
        conn, cursor = create_connection()
        cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
        todo = cursor.fetchone()

        if not todo:
            return {"error": "Todo not found"}, 404

        cursor.execute("""
            UPDATE todos 
            SET title = ?, description = ?, completed = ?
            WHERE id = ?
        """, (data.get("title", todo["title"]),
              data.get("description", todo["description"]),
              int(data.get("completed", todo["completed"])),
              todo_id))

        conn.commit()
        conn.close()
        return {"message": "Todo updated"}

    def delete(self, todo_id):
        """Delete a todo"""
        conn, cursor = create_connection()
        cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        conn.commit()
        conn.close()

        return {"message": "Todo deleted"}
