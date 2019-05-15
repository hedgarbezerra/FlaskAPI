from Models.DB import db, ma


"""Importando do arquivo db as variáveis criadas para conexão e serialização do banco"""


class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    gateway = db.Column(db.String(15), nullable=False)

    def __init__(self, name, type, gateway):
        self.name = name
        self.type = type
        self.gateway = gateway


class DevicesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'type', 'gateway')


device_schema = DevicesSchema(strict=True)
devices_schema = DevicesSchema(many=True)
