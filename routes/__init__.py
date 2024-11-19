# routes/__init__.py
from .contact import contact_bp
from .about import about_bp  # 假設有一個 about Blueprint
from .home import home_bp
from .snake import snake_bp
def init_app(app):
    app.register_blueprint(contact_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(snake_bp)

