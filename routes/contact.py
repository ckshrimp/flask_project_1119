# contact.py
from flask import Blueprint, render_template, request

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f"Thank you, {name}, for your message!"
    return render_template('contact.html')
