import configparser
import os

import markdown
from flask import Flask, request, redirect, url_for

from Models.DB import db, ma
from Views import DevicesView, UsersView

app = Flask(__name__)
# TODO: event handlers e autenticação JWT

# Lê o diretório do arquivo atual
basedir = os.path.abspath(os.path.dirname(__file__))

# Ler as configurações do banco de um arquivo
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


@app.route('/v1/', methods=['GET'])
def index():
    # Usa o os para abrir o arquivo README diretamente da raiz do projeto a partir da basedir
    with open(basedir + '/README.md', 'r', encoding='utf-8') as readme:
        content = readme.read()
        # O markdown converte para HTML
        return markdown.markdown(content)


@app.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('index')), 301


"""Criando o CRUD dos dispositivos(devices)"""


@app.route('/v1/devices', methods=['GET'])
def get_devices():
    return DevicesView.get_devices()


@app.route('/v1/devices/<id>', methods=['GET'])
def get_device(id):
    return DevicesView.get_device(id)


@app.route('/v1/devices', methods=['POST'])
def post_device():
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    return DevicesView.post_device(name, desc, gateway)


@app.route('/v1/devices/<id>', methods=['PUT'])
def update_device(id):
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    data = DevicesView.update_device(id, name, desc, gateway)
    return data


@app.route('/v1/devices/<id>', methods=['DELETE'])
def delete_device(id):
    data = DevicesView.delete_device(id)
    return data


"""Rotas para usuário"""


@app.route('/v1/users', methods=['GET'])
def get_users():
    return UsersView.get_users()


@app.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
    return UsersView.get_user(id)


@app.route('/v1/users', methods=['POST'])
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    return UsersView.post_user(username, password, name, email)


@app.route('/v1/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    return UsersView.update_user(id, username, password, name, email)


@app.route('/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    return UsersView.delete_user(id)


if __name__ == '__main__':

    app.run(debug=True)
