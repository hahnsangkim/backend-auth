from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


engine = create_engine('sqlite:///users.db')
User.metadata.create_all(engine)