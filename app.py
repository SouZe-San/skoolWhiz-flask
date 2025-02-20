from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api
from src.routes.routes import TodoListResource, TodoResource
from src.database import db_initialize
import logging
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
Swagger(app)
# for CORS
# CORS(app, upports_credentials=True, origins=["<URL>"])

# Initialize database from schema.sql
db_initialize()


# Sample data storage
data_storage = "Hello ! this is Prediction API"


def get_data():
    return data_storage


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!\n add /api/ for GET and POST requests.", 200


# Register API routes
api.add_resource(TodoListResource, "/todos")
api.add_resource(TodoResource, "/todos/<int:todo_id>")


# Logging
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    print("⚙️ Flask API server live  🚀")
    app.run(debug=True)
