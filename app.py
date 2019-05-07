from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import configparser
import markdown
import os
from models import Device

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

# Instância do banco de dados
db = SQLAlchemy(app)

# Instancia do serializador Marshmallow
ma = Marshmallow(app)


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









if __name__ == '__main__':
    app.run()
