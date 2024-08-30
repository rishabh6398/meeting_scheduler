# website/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from .main_routes import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    with app.app_context():
        db.create_all()

    return app