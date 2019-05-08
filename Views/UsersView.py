from flask import jsonify

from Models import User
from app import db


def get_users():
    users = User.User.query.all()

    if users:
        result = User.users_schema.dump(users)
        return jsonify({'data': result.data, 'message': 'Success'}), 200

    return jsonify({'message': 'nothing found', 'data': {}})


def get_user(id):

    user = User.User.query.get(id)
    if user:
        return User.user_schema.jsonify(user)

    return jsonify({'message': 'nothing found', 'data': {}})


def post_user(username, password, name, email):
    username = username
    password = password
    name = name
    email = email
    user = User.User(username, password, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        return User.user_schema.jsonify(user)

    except RuntimeError:
        return jsonify({'message': 'unable to create'})


def update_user(id, username, password, name, email):
    user = User.User.query.get(id)
    username = username
    password = password
    name = name
    email = email

    if user:
        user.username = username
        user.password = password
        user.name = name
        user.email = email
        db.session.commit()
        return User.user_schema.jsonify(user)

    else:
        return jsonify({'message': 'unable to update'})


def delete_user(id):
    user = User.User.query.get(id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return User.user_schema.jsonify(user)

    else:
        return jsonify({'message': 'unable to delete'})
