# about.py
from flask import Blueprint, render_template, request

about_bp = Blueprint('about', __name__)

@about_bp.route('/about', methods=['GET', 'POST'])
def about():
     return render_template('about.html', name="Flask User")  # 渲染 about.html 頁面
