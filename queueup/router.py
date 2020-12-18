from datetime import datetime
import requests, json
from flask import request, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from queueup import app, db, oauth, config
from queueup.models import User


@app.route("/", methods=['GET', 'POST'])
def landing_page():
    def index():
        if current_user.is_authenticated:
            return (
                "<p>Hello, {}! You're logged in! Email: {}</p>"
                "<div><p>Google Profile Picture:</p>"
                '<img src="{}" alt="Google profile pic"></img></div>'
                '<a class="button" href="/logout">Logout</a>'.format(
                    current_user.name, current_user.email, current_user.profile_pic
                )
            )
        else:
            return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = app.get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = oauth.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="/authorized",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/authorized", methods=['POST'])
def authorized():
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = app.get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = oauth.prepare_token_request(token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(token_url, headers=headers, data=body,
                                   auth=(config['GOOGLE_CLIENT_ID'], config['GOOGLE_CLIENT_SECRET']),
    )

    # Parse the tokens!
    oauth.parse_request_body_response(json.dumps(token_response.json()))




# @app.route("/create_profile", methods=['POST'])
# def create_profile():
#     return
#
#
# #get everyone on the list
# @app.route("/find_duos", methods=['GET'])
# def get_duos():
#     return
#
#
# #used for profiles on find_duos and used on profile page for current user info
# @app.route("/user/<int:post_id>", methods=['GET'])
# def get_user():
#     return
#
#
# # when you change profile
# @app.route("/profile", methods=['POST'])
# def edit_profile():
#     return


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


