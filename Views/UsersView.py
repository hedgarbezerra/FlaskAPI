from flask import jsonify
from werkzeug import security
from Models import User
from app import db


def get_users():
    users = User.User.query.all()

    if users:
        result = User.users_schema.dump(users)
        return jsonify({'message': 'success', 'data': result.data}), 200

    return jsonify({'message': 'nothing found', 'data': []})


def get_user(id):

    user = User.User.query.get(id)
    if user:
        return User.user_schema.jsonify(user)

    return jsonify({'message': 'nothing found', 'data': []})


def post_user(username, password, name, email):
    if user_by_username(username):
        return jsonify({'message': 'user already exists', 'data': []})

    username = username
    password = password
    name = name
    email = email
    pass_hash = security.generate_password_hash(password)
    user = User.User(username, pass_hash, name, email)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'successfully fetched', 'data': User.user_schema.jsonify(user)}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': []}), 500


def update_user(id, username, password, name, email):
    user = User.User.query.get(id)
    username = username
    password = password
    name = name
    email = email
    pass_hash = security.generate_password_hash(password)

    if user:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        return jsonify({'message': 'successfully fetched', 'data': User.user_schema.jsonify(user)}), 200

    else:
        return jsonify({'message': 'unable to update', 'data': []}), 500


def delete_user(id):
    user = User.User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'successfully fetched', 'data':User.user_schema.jsonify(user)}), 202
    else:
        return jsonify({'message': 'unable to delete', 'data': []}), 404


def user_by_username(username):
    try:
        return User.User.query.filter(User.User.username == username).one()
    except:
        return None


