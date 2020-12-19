from datetime import datetime
import requests, json
from flask import request, redirect, url_for, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from queueup import app, db, oauth, get_google_provider_cfg
from queueup.models import User


@app.route("/", methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.picture
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = oauth.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url+"/authorized",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/authorized", methods=['GET', 'POST'])
def authorized():
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = oauth.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(app.config['GOOGLE_CLIENT_ID'], app.config['GOOGLE_CLIENT_SECRET']),
    )

    # Parse the tokens!
    oauth.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = oauth.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)


    # verify their email through Google
    if userinfo_response.json().get("email_verified"):
        id = userinfo_response.json()["sub"]
        email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400


    # Create a user in db with the information provided by Google
    user = User(id=id, name=name, email=email, picture=picture)

    # Doesn't exist? Add it to the database.
    #if not User.query.filter_by(id=id).first():
    if not User.query.get(id):
        db.session.add(user)
        db.session.commit()

    # Begin user session by logging the user in
    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/create_profile", methods=['POST'])
def create_profile():
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route("/users/getmatches", methods=['GET'])
def get_matches():
    users = User.query.all()
    users = [user.serialize() for user in users]

    for user in users:
        print(user)
        # logic for getting matches

    return jsonify(users)

#used for profiles on find_duos and used on profile page for current user info
@app.route("/user/<int:user_id>", methods=['GET'])
def get_user():
    return


# #get everyone on the list
# @app.route("/find_duos", methods=['GET'])
# def get_duos():
#     return
#
# # when you change profile
# @app.route("/profile", methods=['POST'])
# def edit_profile():
#     return