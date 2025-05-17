from flask import Blueprint, render_template

vpc_bp = Blueprint('vpc', __name__, url_prefix='/vpc')

@vpc_bp.route('/')
def index():
    # Render a VPC-specific HTML page
    return render_template('vpc.html')
