from . import db
from flask_login import UserMixin

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"Task set with the id {self.id}"
    

class User(db.Model, UserMixin):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"You have successfully registered with username {self.username}"