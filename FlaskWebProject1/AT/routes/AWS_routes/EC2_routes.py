from flask import Blueprint, render_template

ec2_bp = Blueprint('ec2', __name__, url_prefix='/ec2')

@ec2_bp.route('/')
def index():
    return render_template('ec2.html')
