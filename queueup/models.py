import time
from flask_sqlalchemy import SQLAlchemy
from queueup import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    picture = db.Column(db.String(100), nullable=False, default='default.jpg')


    # profile info fill in later
    # posts = db.relationship('Post', backref='author', lazy=True)
    # roles, opggLink, matches = , swipedLeft
    # swipedRight

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


'''
if initializing the db for the first time run the following code in the python shell: 

from queueup import db
from queueup.models import User, <other models you want to create a table for>, 
db.create_all()
'''
