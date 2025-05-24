
from flask import Blueprint, abort, render_template, request, redirect, url_for
from AT import db
from bson.objectid import ObjectId

terra_modules_bp = Blueprint('tmod', __name__, url_prefix='/tmod')

@terra_modules_bp.route('/architectures/<arch_id>/add-modules')
def add_terra_modules(arch_id): 
 
    architecture = db.aws_architecture_table.find_one({"_id": ObjectId(arch_id)})

    if architecture:
        arch_name = architecture.get("architecture_name", "Unknown Architecture")
    else:
        arch_name = "Unknown Architecture"

    modules = list(db.Terraform_module.find())

    return render_template(
        'aws/add_terra_modules.html', 
        arch_id=arch_id,      
        arch_name=arch_name,  
        modules=modules
    )


  