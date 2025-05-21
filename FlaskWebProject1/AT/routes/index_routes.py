

from datetime import datetime
from flask import render_template, request
from AT import app,db

from bson.objectid import ObjectId
from flask import redirect, url_for, request
 
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# @app.route('/aws_dashboard')
# def aws_dashboard():
#     architectures = list(db["aws_architecture_table"].find()) 
#     for arch in architectures:
#         arch['_id'] = str(arch['_id'])
#     return render_template('aws_dashboard.html', architectures=architectures)


# @app.route('/create_aws_architecture')
# def create_aws_architecture():
#      AWS_Category= db["Services_by_category"]
#      data = list(AWS_Category.find())
#      print(data)
#      return render_template(
#         'create_aws_architecture.html',
#         title='AWS',
#         data=data
       
#     ) 




# @app.route('/create_architecture', methods=['POST'])
# def create_architecture():
#     architecture_name = request.form.get('architecture_name')
#     selected_services = request.form.getlist('services')

#     print("Architecture Name:", architecture_name)
#     print("Selected Services:", selected_services)
     
#     db["aws_architecture_table"].insert_one({
#         "architecture_name": architecture_name,
#         "services": selected_services
#     })
     
#     return redirect(url_for('aws_dashboard'))






# @app.route('/delete_architecture/<arch_id>', methods=['POST'])
# def delete_architecture(arch_id):
#     try:
#         db["aws_architecture_table"].delete_one({"_id": ObjectId(arch_id)})
#         print(f"Deleted architecture with id: {arch_id}")
#     except Exception as e:
#         print(f"Error deleting architecture: {e}")
#     return redirect(url_for('aws_dashboard'))





@app.route('/GCP')
def GCP():
    """Renders the about page."""
    return render_template(
        'GCP.html',
        title='GCP',
        message='Your Page description GCP page.'
    )


@app.route('/AZURE')
def AZURE():
    """Renders the about page."""
    return render_template(
        'AZURE.html',
        title='AZURE',
        message='Your Page description AZURE page.'
    )

