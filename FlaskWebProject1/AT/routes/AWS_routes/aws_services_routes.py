# servicename_routes.py

from flask import Blueprint, render_template

aws_service_bp = Blueprint('aws_service_bp', __name__)

@aws_service_bp.route('/aws/<service_name>')
def aws_service(service_name):
    # You can use service_name to decide what to render
    return render_template('aws_service.html', service_name=service_name)
