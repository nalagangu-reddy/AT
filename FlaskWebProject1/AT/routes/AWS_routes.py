from flask import Blueprint, abort, render_template, request, redirect, url_for
from AT import db
from bson.objectid import ObjectId

aws_bp = Blueprint('aws', __name__, url_prefix='/aws')


# --- Utility Functions ---

def get_services_by_category():
    """Retrieve service categories from the database."""
    return list(db["Services_by_category"].find())

def parse_selected_services(service_list):
    """Convert flat selected services into a dictionary grouped by category."""
    grouped_services = {}
    for item in service_list:
        if "::" in item:
            category, service = item.split('::', 1)
            grouped_services.setdefault(category, []).append(service)
    return grouped_services

def get_architecture_by_id(arch_id):
    """Fetch architecture and convert _id to str."""
    try:
        architecture = db["aws_architecture_table"].find_one({"_id": ObjectId(arch_id)})
        if architecture:
            architecture['_id'] = str(architecture['_id'])
        return architecture
    except Exception:
        return None


# --- Routes ---

@aws_bp.route('/create_aws_architecture')
def create_aws_architecture():
    return render_template(
        'aws/create_aws_architecture.html',
        title='AWS',
        data=get_services_by_category()
    )


@aws_bp.route('/create_architecture', methods=['POST'])
def create_architecture():
    architecture_name = request.form.get('architecture_name')
    selected_services = parse_selected_services(request.form.getlist('services'))

    db["aws_architecture_table"].insert_one({
        "architecture_name": architecture_name,
        "services": selected_services
    })

    return redirect(url_for('aws.aws_dashboard'))


@aws_bp.route('/edit_aws_architecture/<arch_id>')
def edit_aws_architecture(arch_id):
    architecture = get_architecture_by_id(arch_id)
    if not architecture:
        return "Architecture not found", 404

    return render_template(
        'aws/edit_aws_architecture.html',
        architecture=architecture,
        data=get_services_by_category(),
        title="AWS"
    )


@aws_bp.route('/update_aws_architecture/<arch_id>', methods=['POST'])
def update_aws_architecture(arch_id):
    architecture_name = request.form.get('architecture_name')
    selected_services = parse_selected_services(request.form.getlist('services'))

    db["aws_architecture_table"].update_one(
        {"_id": ObjectId(arch_id)},
        {"$set": {
            "architecture_name": architecture_name,
            "services": selected_services
        }}
    )

    return redirect(url_for('aws.aws_dashboard'))


@aws_bp.route('/architectures/<arch_id>/view')
def view_aws_architecture(arch_id):
    architecture = get_architecture_by_id(arch_id)
    if not architecture:
        abort(404)
    return render_template('aws/view_aws_architecture.html', architecture=architecture)




@aws_bp.route('/aws_dashboard')
def aws_dashboard():
    architectures = list(db["aws_architecture_table"].find())
    for arch in architectures:
        arch['_id'] = str(arch['_id'])
    return render_template('aws/aws_dashboard.html', architectures=architectures)


@aws_bp.route('/delete_architecture/<arch_id>', methods=['POST'])
def delete_architecture(arch_id):
    try:
        db["aws_architecture_table"].delete_one({"_id": ObjectId(arch_id)})
        print(f"Deleted architecture with id: {arch_id}")
    except Exception as e:
        print(f"Error deleting architecture: {e}")
    return redirect(url_for('aws.aws_dashboard'))
