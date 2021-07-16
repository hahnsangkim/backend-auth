from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()
app = Flask(__name__)
app.config.update(
    SECRET_KEY='thisissectretkeyfordashflaskapp',
    SQLALCHEMY_DATABASE_URI='sqlite:///users.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

def create_app():
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = '/'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app