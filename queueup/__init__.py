import json, os, requests
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient
from flask_login import login_user, current_user, logout_user, login_required
from flask_cors import CORS
from flask_socketio import SocketIO, send, join_room, emit

# flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('join')
def joinRoom(data):
    room = data['room']
    join_room(room)
    emit('privateMessage', "Private room entered", room=room)

@socketio.on('privateMessage')
def handlePrivateMessage(msg, data):
    room = data['room']
    print(data, flush=True) 
    emit('privateMessage', msg, room=room)

# database info
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# google oauth info
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #change when we go to prod
# app.config['GOOGLE_CLIENT_ID'] = os.environ.get("GOOGLE_CLIENT_ID", None)
# app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get("GOOGLE_CLIENT_SECRET", None)
app.config['GOOGLE_CLIENT_ID'] = '288719160483-ufo1sv5hl6618lcecbh6hgci9p9eoq74.apps.googleusercontent.com'
app.config['GOOGLE_CLIENT_SECRET'] = 'k6lLl8zstbNcEbVpqQzeU1PK'

app.config['GOOGLE_DISCOVERY_URL'] = "https://accounts.google.com/.well-known/openid-configuration"

def get_google_provider_cfg():
    return requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()

###### user session management ######
login_manager = LoginManager()
login_manager.init_app(app)
#######################################

db = SQLAlchemy(app)
oauth = WebApplicationClient(app.config['GOOGLE_CLIENT_ID'])


from queueup import router
