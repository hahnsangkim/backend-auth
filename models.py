from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
# from passlib.apps import custom_app_context as pwd_context
from werkzeug.security import generate_password_hash, check_password_hash


from flask_login import UserMixin
from config import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), index=True, unique=True, nullable=False)
    password = Column(String(124))

    def hash_password(self, password):
        # self.password = pwd_context.hash(password)
        self.password = generate_password_hash(password, method='sha256')

    def verify_password(self, password):
        # return pwd_context.verify(password, self.password)
        return check_password_hash(self.password, password)

# engine = create_engine('sqlite:///users.db', connect_args={'check_same_thread': False})
# User.metadata.create_all(engine)