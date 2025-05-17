"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from AT import app,db

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


@app.route('/AWS')
def AWS():
    """Get data from the 'service_category' collection dynamically."""
    service_category_collection = db["service_category"]
    data = list(service_category_collection.find())
    return render_template(
        'AWS.html',
        title='AWS',
        data=data
    )


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

