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

    opggLink = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)
    userRank = db.Column(db.Integer, nullable=True)
    highRankLF = db.Column(db.Integer, nullable=True)
    lowRankLF = db.Column(db.Integer, nullable=True)

    profileCreated = db.Column(db.Boolean, nullable=False, default=False)

    #roles = db.relationship('Role', backref='user_id', lazy=True)
    # swipedDown =
    # swipedUp =
    # matches

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'picture': self.picture,
                'opggLink': self.opggLink, 'description': self.description, 'userRank': self.userRank,
                'highRankLF': self.highRankLF, 'lowRankLF': self.lowRankLF}


class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    role_name = db.Column(db.String(50))
    roles_wanted = db.Column(db.Boolean, nullable=False)

    def serialize(self):
        return {'user_id': self.user_id, 'role_name': self.role_name, 'roles_wanted': self.roles_wanted}

'''
if initializing the db for the first time run the following code in the python shell: 

from queueup import db
from queueup.models import User, <other models you want to create a table for>, 
db.create_all()
'''
