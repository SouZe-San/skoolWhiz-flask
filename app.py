from flask import Flask
from flask_restx import Api
from src.routes.routes import api as todo_api
from src.database import db_initialize
import logging

app = Flask(__name__)

# Initialize database from schema.sql
db_initialize()


@app.route('/', methods=['GET'])
def home():
    """
        Api Alive Check
        ---
        responses:
            200:
                description: A successful response
                examples:
                    application/text: "Welcome 🚀"
    """
    return "Welcome 🚀", 200


# Swagger API Documentation
api = Api(app, title="Todo API",
          description="A simple Todo API using Flask", version="1.0", doc="/api/docs")

# Register API namespace
api.add_namespace(todo_api, path="/todos")


# Logging
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    print("⚙️ Flask API server live  🚀")
    app.run(debug=True)
