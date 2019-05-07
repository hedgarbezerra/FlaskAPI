from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import configparser
import markdown
import os
from models import Device, User
from models.DB import db, ma

app = Flask(__name__)


# Lê o diretório do arquivo atual
basedir = os.path.abspath(os.path.dirname(__file__))

# Ler as configurações de rota do banco de um arquivo
config = configparser.ConfigParser()
config.read(f'{basedir}/config.ini')
user = config['DATABASE']['user']
passwd = config['DATABASE']['passwd']
dbc = config['DATABASE']['db']
host = config['DATABASE']['host']
port = int(config['DATABASE']['port'])

# Definições do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{passwd}@{host}:{port}/{dbc}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)
"""Definindo as rotas"""

"""O index além do login será única parte visual da API(Mostrando a documentação)"""


@app.route('/', methods=['GET'])
def index():
    # Usa o os para abrir o arquivo README diretamente da raiz do projeto a partir da basedir
    with open(basedir + '/README.md', 'r') as readme:
        content = readme.read()
        # O markdown converte para HTML
        return markdown.markdown(content)


"""Criando o CRUD dos dispositivos(devices)"""


@app.route('/device', methods=['GET'])
def get_devices():
    devices = Device.Device.query.all()
    result = Device.devices_schema.dump(devices)
    return jsonify(result.data)


@app.route('/device/<id>', methods=['GET'])
def get_device(id):
    device = Device.Device.query.get(id)
    return Device.device_schema.jsonify(device)


@app.route('/device', methods=['POST'])
def post_device():
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    device = Device.Device(name, desc, gateway)
    db.session.add(device)
    db.session.commit()

    return Device.device_schema.jsonify(device)


@app.route('/device/<id>', methods=['PUT'])
def update_device(id):
    device = Device.Device.query.get(id)
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    device.name = name
    device.desc = desc
    device.gateway = gateway

    db.session.commit()

    return Device.device_schema.jsonify(device)


@app.route('/device/<id>', methods=['DELETE'])
def delete_device(id):
    device = Device.Device.query.get(id)
    db.session.delete(device)
    db.session.commit()

    return Device.device_schema.jsonify(device)


"""Rotas para usuário"""


@app.route('/user', methods=['GET'])
def get_users():
    users = User.User.query.all()
    result = User.users_schema.dump(users)
    return jsonify(result.data)


@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.User.query.get(id)
    return User.user_schema.jsonify(user)


@app.route('/user', methods=['POST'])
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    userr = User.User(username, password, name, email)
    db.session.add(userr)
    db.session.commit()

    return User.user_schema.jsonify(userr)


@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    userr = User.User.query.get(id)
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    userr.username = username
    userr.password = password
    userr.name = name
    userr.email = email

    db.session.commit()

    return User.user_schema.jsonify(user)


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    userr = User.User.query.get(id)
    db.session.delete(userr)
    db.session.commit()

    return User.user_schema.jsonify(userr)




if __name__ == '__main__':
    app.run()
