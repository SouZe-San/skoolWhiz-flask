from flask import Blueprint, request, jsonify
import sqlite3
from src.database import create_connection

todo_bp = Blueprint("todos", __name__)


@todo_bp.route("/", methods=["GET"])
def get_todos():
    """
    Retrieve all todo items
    ---
    responses:
        200:
            description: A list of todo items
            examples:
                application/json:
                    [
                        {"id": 1, "title": "Task", "description": "Details", "completed": false}
                    ]
    """
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    print(todos)
    conn.close()

    return jsonify([
        {"id": row[0], "title": row[1],
            "description": row[2], "completed": bool(row[3])}
        for row in todos
    ]), 200


@todo_bp.route("/", methods=["POST"])
def create_todo():
    """
    Create a new todo item
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
            type: object
            required:
                - title
            properties:
                title:
                    type: string
                    description: The title of the task
                description:
                    type: string
                    description: Task details
    responses:
        201:
            description: Todo created successfully
            examples:
                application/json:
                    {
                        "message": "Todo created",
                        "id": 1
                    }
    """
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    conn, cursor = create_connection()
    cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)",
                   (data["title"], data.get("description", "")))
    conn.commit()
    todo_id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Todo created", "id": todo_id}), 201


@todo_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    """
    Retrieve a single todo item
    ---
    parameters:
      - name: todo_id
        in: path
        required: true
        type: integer
        description: The ID of the todo item
    responses:
        200:
            description: A single todo item
            examples:
                application/json: {"id": 1, "title": "Sample Task", "description": "Details", "completed": false}
        404:
            description: Todo not found
    """
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    todo = cursor.fetchone()
    conn.close()

    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify({"id": todo[0], "title": todo[1], "description": todo[2], "completed": bool(todo[3])}), 200


@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    """
    Update a todo item
    ---
    parameters:
      - name: todo_id
        in: path
        required: true
        type: integer
        description: The ID of the todo item
      - name: body
        in: body
        required: true
        schema:
            type: object
            properties:
                title:
                    type: string
                description:
                    type: string
                completed:
                    type: boolean
    responses:
        200:
            description: Todo updated successfully
            examples:
                application/json: {"message": "Todo updated"}
        404:
            description: Todo not found
    """
    data = request.get_json()
    conn, cursor = create_connection()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    todo = cursor.fetchone()

    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    cursor.execute("""
        UPDATE todos 
        SET title = ?, description = ?, completed = ?
        WHERE id = ?
    """, (data.get("title", todo[1]),
          data.get("description", todo[2]),
          int(data.get("completed", todo[3])),
          todo_id))

    conn.commit()
    conn.close()
    return jsonify({"message": "Todo updated"}), 200


@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    """
    Delete a todo item
    ---
    parameters:
      - name: todo_id
        in: path
        required: true
        type: integer
        description: The ID of the todo item
    responses:
        200:
            description: Todo deleted successfully
            examples:
                application/json: {"message": "Todo deleted"}
        404:
            description: Todo not found
    """
    conn, cursor = create_connection()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Todo deleted"}), 200
