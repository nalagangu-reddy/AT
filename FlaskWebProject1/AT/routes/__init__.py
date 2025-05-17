"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import AT.routes.AWS_routes 