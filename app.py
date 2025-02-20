from flask import Flask
from flask_restful import Api
from src.routes.routes import todo_bp
from src.database import db_initialize
import logging
from flasgger import Swagger

app = Flask(__name__)
# api = Api(app)

Swagger(app, template={
    "info": {
        "title": "My Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})

# Initialize database from schema.sql
db_initialize()


@app.route('/', methods=['GET'])
def home():
    """
        This is an Test Url
        ---
        responses:
            200:
                description: A successful response
                examples:
                    application/text: "Welcome 🚀"
    """
    return "Welcome 🚀", 200


# Register API routes
app.register_blueprint(todo_bp, url_prefix='/todos')


# Logging
logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    print("⚙️ Flask API server live  🚀")
    app.run(debug=True)
