"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from AT import app
from pymongo import MongoClient
from AT.routes.AWS_routes import aws_bp



app.register_blueprint(aws_bp)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = 5555
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
