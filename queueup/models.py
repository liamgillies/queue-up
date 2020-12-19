import time
from flask_sqlalchemy import SQLAlchemy
from queueup import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    picture = db.Column(db.String(20), nullable=False, default='default.jpg')


    # profile info fill in later
    # posts = db.relationship('Post', backref='author', lazy=True)
    # roles, opggLink, matches = , swipedLeft
    # swipedRight

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"