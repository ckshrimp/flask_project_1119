from flask import Flask, render_template, request, flash
from routes import init_app

app = Flask(__name__)
init_app(app)  # 初始化並註冊所有 Blueprint

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
