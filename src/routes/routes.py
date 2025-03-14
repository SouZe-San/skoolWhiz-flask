from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
import sqlite3
from src.database import create_connection

api = Namespace("todos", description="Todo CRUD operations")

# Define Swagger Models
todo_model = api.model("Todo", {
    "id": fields.Integer(readonly=True, description="The unique identifier"),
    "title": fields.String(required=True, description="Title of the task"),
    "description": fields.String(description="Task description"),
    "completed": fields.Boolean(default=False, description="Completion status")
})

todo_create_model = api.model("TodoCreate", {
    "title": fields.String(required=True, description="Title of the task"),
    "description": fields.String(description="Task description")
})

todo_update_model = api.model("TodoUpdate", {
    "title": fields.String(description="Updated title"),
    "description": fields.String(description="Updated description"),
    "completed": fields.Boolean(description="Updated completion status")
})


@api.route("/")
class TodoListResource(Resource):
    @api.doc("list_todos")
    @api.marshal_list_with(todo_model)
    def get(self):
        """Retrieve all todos"""
        try:
            conn, cursor = create_connection()
            cursor.execute("SELECT * FROM todos")
            todos = cursor.fetchall()
            conn.close()

            return [
                {"id": row[0], "title": row[1],
                    "description": row[2], "completed": bool(row[3])}
                for row in todos
            ]
        except sqlite3.Error as e:
            print("(db) From get TODOS: ", e)
            return {"error": "Query Issus"}, 408
        except Exception as e:
            print("From get TODOS: ", e)
            return {"error": "Unknown Error"}, 500

    @api.doc("create_todo")
    @api.expect(todo_create_model)
    def post(self):
        """Create a new todo"""
        data = request.get_json()
        if "title" not in data:
            return {"error": "Title is required"}, 406
        if not isinstance(data["title"], str):
            return jsonify({"error": "Title must be a string"}), 406
        if "description" in data and not isinstance(data["description"], str):
            return jsonify({"error": "Description must be a string"}), 406

        try:
            conn, cursor = create_connection()
            cursor.execute("INSERT INTO todos (title, description) VALUES (?, ?)",
                           (data["title"], data.get("description", "")))
            conn.commit()
            todo_id = cursor.lastrowid
            conn.close()

            return {"message": "Todo created", "id": todo_id}, 201
        except sqlite3.Error as e:
            print("(db) From create TODOS: ", e)
            return {"error": "Query Issus"}, 408
        except Exception as e:
            print("From create TODOS: ", e)
            return {"error": "Unknown Error"}, 500


@api.route("/<int:todo_id>")
@api.response(404, "Todo not found")
class TodoResource(Resource):
    @api.doc("get_todo")
    @api.marshal_with(todo_model)
    def get(self, todo_id):
        """Retrieve a single todo"""
        try:
            conn, cursor = create_connection()
            cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
            todo = cursor.fetchone()
            conn.close()

            if not todo:
                return {"error": "Todo not found"}, 404

            return {"id": todo[0], "title": todo[1], "description": todo[2], "completed": bool(todo[3])}
        except sqlite3.Error as e:
            print("(db) From get TODO: ", e)
            return {"error": "Query Issus"}, 408
        except Exception as e:
            print("From get TODO: ", e)
            return {"error": "Unknown Error"}, 500

    @api.doc("update_todo")
    @api.expect(todo_update_model)
    def put(self, todo_id):
        """Update a todo"""
        data = request.get_json()
        if "title" not in data:
            return jsonify({"error": "Title is required"}), 406
        if not isinstance(data["title"], str):
            return jsonify({"error": "Title must be a string"}), 406
        if "description" in data and not isinstance(data["description"], str):
            return jsonify({"error": "Description must be a string"}), 406
        if "completed" in data and not isinstance(data["completed"], bool):
            return jsonify({"error": "completed must be a boolean"}), 406

        try:
            conn, cursor = create_connection()
            cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
            todo = cursor.fetchone()

            if not todo:
                return {"error": "Todo not found"}, 404

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
            return {"message": "Todo updated"}
        except sqlite3.Error as e:
            print("(db) From update TODO: ", e)
            return {"error": "Query Issus"}, 408
        except Exception as e:
            print("From update TODO: ", e)
            return {"error": "Unknown Error"}, 500

    @api.doc("delete_todo")
    def delete(self, todo_id):
        """Delete a todo"""
        try:
            conn, cursor = create_connection()
            cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
            conn.commit()
            conn.close()

            return {"message": "Todo deleted"}
        except sqlite3.Error as e:
            print("(db) From delete TODO: ", e)
            return {"error": "Query Issus"}, 408
        except Exception as e:
            print("From delete TODO: ", e)
            return {"error": "Unknown Error"}, 500
