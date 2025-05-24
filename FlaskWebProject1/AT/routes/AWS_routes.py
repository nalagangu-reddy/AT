from flask import Blueprint, render_template, request, redirect, url_for
from AT import db  # import your db instance from your app package
from bson.objectid import ObjectId
aws_bp = Blueprint('aws', __name__, url_prefix='/aws')  

@aws_bp.route('/create_aws_architecture')
def create_aws_architecture():
    AWS_Category = db["Services_by_category"]
    data = list(AWS_Category.find())
    print(data)
    return render_template(
        'create_aws_architecture.html',
        title='AWS',
        data=data
    )

@aws_bp.route('/create_architecture', methods=['POST'])
def create_architecture():
    architecture_name = request.form.get('architecture_name')
    selected_services_raw = request.form.getlist('services')

    # Group by category
    services_by_category = {}
    for item in selected_services_raw:
        category, service = item.split('::', 1)
        if category not in services_by_category:
            services_by_category[category] = []
        services_by_category[category].append(service)

    # Save to DB
    db["aws_architecture_table"].insert_one({
        "architecture_name": architecture_name,
        "services": services_by_category
    })

    return redirect(url_for('aws.aws_dashboard'))

@aws_bp.route('/edit_aws_architecture/<arch_id>', methods=['GET'])
def edit_aws_architecture(arch_id):
    # Fetch architecture record by ID
    architecture = db["aws_architecture_table"].find_one({"_id": ObjectId(arch_id)})
    if not architecture:
        return "Architecture not found", 404

    architecture['_id'] = str(architecture['_id'])

    # Convert service list into a dictionary grouped by category
    services_raw = architecture.get('services', [])
    if isinstance(services_raw, list):
        services_by_category = {}
        for item in services_raw:
            if "::" in item:
                category, service = item.split('::', 1)
                services_by_category.setdefault(category, []).append(service)
        architecture['services'] = services_by_category

    # Get full service list grouped by category (used for UI dropdowns or display)
    AWS_Category = db["Services_by_category"]
    data = list(AWS_Category.find())  # Same as used in create_aws_architecture

    return render_template(
        'edit_aws_architecture.html',
        architecture=architecture,
        data=data,  # services grouped by category
        title="AWS"
    )


@aws_bp.route('/update_aws_architecture/<arch_id>', methods=['POST'])
def update_aws_architecture(arch_id):
    architecture_name = request.form.get('architecture_name')
    selected_services_raw = request.form.getlist('services')

    services_by_category = {}
    for item in selected_services_raw:
        category, service = item.split('::', 1)
        services_by_category.setdefault(category, []).append(service)

    db["aws_architecture_table"].update_one(
        {"_id": ObjectId(arch_id)},
        {"$set": {
            "architecture_name": architecture_name,
            "services": services_by_category
        }}
    )

    return redirect(url_for('aws.aws_dashboard'))


@aws_bp.route('/aws_dashboard')
def aws_dashboard():
     architectures = list(db["aws_architecture_table"].find())
     for arch in architectures:
          arch['_id'] = str(arch['_id'])
     print(architectures)
     return render_template('aws_dashboard.html', architectures=architectures)



@aws_bp.route('/delete_architecture/<arch_id>', methods=['POST'])
def delete_architecture(arch_id):
    try:
        db["aws_architecture_table"].delete_one({"_id": ObjectId(arch_id)})
        print(f"Deleted architecture with id: {arch_id}")
    except Exception as e:
        print(f"Error deleting architecture: {e}")
    return redirect(url_for('aws.aws_dashboard'))
