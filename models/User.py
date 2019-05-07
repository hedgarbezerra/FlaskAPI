from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from models.DB import db, ma


"""Importando do arquivo db as variáveis criadas para conexão e serialização do banco"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.sysdate())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email')


user_schema = UserSchema(strict=True)
users_schema = UserSchema(strict=True, many=True)