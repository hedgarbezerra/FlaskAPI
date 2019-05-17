from Models.DB import db, ma
import datetime


class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    gateway = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    user = db.relationship('Users', back_populates='devices')

    def __init__(self, name, type, gateway, user_id):
        self.name = name
        self.type = type
        self.gateway = gateway
        self.user_id = user_id

class DevicesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'type', 'gateway', 'user_id', 'created_at')