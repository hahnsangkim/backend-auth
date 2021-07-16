from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = SQLAlchemy()
app = Flask(__name__)
app.config.update(
    SECRET_KEY='thisissectretkeyfordashflaskapp',
    SQLALCHEMY_DATABASE_URI='sqlite:///users.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
)

engine = create_engine('sqlite:///users.db',connect_args={'check_same_thread': False})
DBSession = sessionmaker(engine)
session = DBSession()

def create_app():
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = '/'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app