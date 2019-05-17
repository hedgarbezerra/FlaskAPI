import configparser
import datetime
import os
import random
import string
from functools import wraps
import jwt
import markdown
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.security import check_password_hash
from Models.DB import db, ma
from Views import DevicesView, UsersView

app = Flask(__name__)

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
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))

# Definições do banco de dados e app
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{passwd}@{host}:{port}/{dbc}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = key
db.init_app(app)
ma.init_app(app)

"""Fazendo a autenticação com JWT e o servidor"""


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated




# Gerando token com base na Secret key do app e definindo expiração com 'exp'

@app.route('/v4/login', methods=['GET', 'POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'),
                        'valid until': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


"""O index além do login será única parte visual da API(Mostrando a documentação)"""


@app.route('/v4/', methods=['GET'])
def index():
    # Usa o os para abrir o arquivo README diretamente da raiz do projeto a partir da basedir
    with open(basedir + '/README.md', 'r', encoding='utf-8') as readme:
        content = readme.read()
        # O markdown converte para HTML
        return markdown.markdown(content)


@app.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('index')), 301


"""Rotas dos dispositivos(devices)"""


@app.route('/v4/devices', methods=['GET'])
@token_required
def get_devices(current_user):
    return DevicesView.get_devices(current_user)


@app.route('/v4/devices/<id>', methods=['GET'])
@token_required
def get_device(current_user, id):
    return DevicesView.get_device(current_user, id)


@app.route('/v4/devices', methods=['POST'])
@token_required
def post_device(current_user):
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    return DevicesView.post_device(name, desc, gateway, current_user)


@app.route('/v4/devices/<id>', methods=['PUT'])
@token_required
def update_device(current_user, id):
    name = request.json['name']
    desc = request.json['desc']
    gateway = request.json['gateway']

    data = DevicesView.update_device(id, name, desc, gateway)
    return data


@app.route('/v4/devices/<id>', methods=['DELETE'])
@token_required
def delete_device(current_user, id):
    data = DevicesView.delete_device(id)
    return data


"""Rotas para usuário"""


@app.route('/v4/users', methods=['GET'])
def get_users():
    return UsersView.get_users()


@app.route('/v4/users/<id>', methods=['GET'])
def get_user(id):
    return UsersView.get_user(id)


@app.route('/v4/users', methods=['POST'])
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    return UsersView.post_user(username, password, name, email)


@app.route('/v4/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    return UsersView.update_user(id, username, password, name, email)


@app.route('/v4/users/<id>', methods=['DELETE'])
def delete_user(id):
    return UsersView.delete_user(id)


if __name__ == '__main__':

    app.run(debug=True)
