import json, os, requests
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient
from queueup.models import User
from flask_login import login_user, current_user, logout_user, login_required


# flask app
app = Flask(__name__)
config = dict()

# database info
config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or os.urandom(24)
config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# google oauth info
config['GOOGLE_CLIENT_ID'] = os.environ.get("GOOGLE_CLIENT_ID", None)
config['GOOGLE_CLIENT_SECRET'] = os.environ.get("GOOGLE_CLIENT_SECRET", None)
config['GOOGLE_DISCOVERY_URL'] = "https://accounts.google.com/.well-known/openid-configuration"

def get_google_provider_cfg():
    return requests.get(config['GOOGLE_DISCOVERY_URL']).json()

###### user session management ######
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#######################################

db = SQLAlchemy(app)
oauth = WebApplicationClient(config['GOOGLE_CLIENT_ID'])


from queueup import router
