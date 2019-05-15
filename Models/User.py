import datetime

from sqlalchemy import func

from Models.DB import db, ma

"""Importando do arquivo db as variáveis criadas para conexão e serialização do banco"""


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(110), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password')


user_schema = UsersSchema(strict=True)
users_schema = UsersSchema(strict=True, many=True)