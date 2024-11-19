# contact.py
from flask import Blueprint, render_template, request

snake_bp = Blueprint('snake', __name__)


@snake_bp.route('/snake', methods=['GET', 'POST'])
def snake():
     return render_template('snake.html', name="Flask User")  