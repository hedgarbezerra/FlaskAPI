from app import db, ma

"""Importando do arquivo db as variáveis criadas para conexão e serialização do banco"""


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(60), nullable=False)
    gateway = db.Column(db.String(15), nullable=False)

    def __init__(self, name, desc, gateway):
        self.name = name
        self.desc = desc
        self.gateway = gateway


class DeviceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'desc', 'gateway')


device_schema = DeviceSchema(strict=True)
devices_schema = DeviceSchema(strict=True, many=True)
