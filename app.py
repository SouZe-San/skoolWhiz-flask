from flask import Flask
from flask_restx import Api
from src.routes.routes import api as todo_api
from src.database import db_initialize
import logging
from flasgger import Swagger

app = Flask(__name__)
# api = Api(app)

# Swagger(app, template={
#     "info": {
#         "title": "My Flask API",
#         "description": "An example API using Flask and Swagger",
#         "version": "1.0.0"
#     }
# })

# Initialize database from schema.sql
db_initialize()


# @app.route('/', methods=['GET'])
# def home():
#     """
#         This is an Test Url
#         ---
#         responses:
#             200:
#                 description: A successful response
#                 examples:
#                     application/text: "Welcome 🚀"
#     """
#     return "Welcome 🚀", 200


# Swagger API Documentation
api = Api(app, title="Todo API",
          description="A simple Todo API using Flask", version="1.0")

# Register API namespace
api.add_namespace(todo_api, path="/todos")


# Logging
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    print("⚙️ Flask API server live  🚀")
    app.run(debug=True)
