from flask import Flask, Blueprint, request, jsonify, make_response, current_app
from website.models import User
import uuid # for public id
from  werkzeug.security import generate_password_hash, check_password_hash
# imports for PyJWT authentication
import jwt
from datetime import datetime, timedelta
from website import db
from website.helpers import getUsersList
from website.token import token_required

auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['POST'])
def signin():
    email = request.json["email"]
    password = request.json["password"]
  
    if not email or not password:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Signin required !!"'}
        )
  
    user = User.query\
        .filter_by(email = email)\
        .first()
  
    if not user:
        return make_response(
            'User with this email does not exist!',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp' : datetime.utcnow() + timedelta(days = 365)
        }, current_app.config['SECRET_KEY'])
  
        return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
    # returns 403 if password is wrong
    return make_response(
            'Password is incorrect!',
            403,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
# signup route
@auth.route('/signup', methods=['POST'])
def signup():
    email = request.json["email"]
    password = request.json["password"]
    first_name = request.json["firstName"]
    last_name = request.json["lastName"]
    username = request.json["username"]
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()

    users = User.query.all()

    if not user:
        # database ORM object
        user = User(
            public_id = str(uuid.uuid4()),
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = generate_password_hash(password)
        )
        if users:
            user.user_type = "staff"
        else:
            user.user_type = "admin"

        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)



@auth.route('/users', methods=['GET'])
@token_required
def users():
    return jsonify(getUsersList(User.query.all()))

@auth.route('/verify-token', methods=['POST'])
@token_required
def verify_token():
    return jsonify({'success': True}), 200

@auth.route('/current-user')
@token_required
def currentUser():
    token = request.headers['x-access-token']
    data = jwt.decode(token, current_app.config['SECRET_KEY'])
    current_user = getUsersList(User.query\
        .filter_by(public_id = data['public_id'])\
        .all())[0]
    return jsonify(current_user)