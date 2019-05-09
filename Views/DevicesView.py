from flask import jsonify

from Models import Device
from app import db


def get_devices():
    devices = Device.Device.query.all()

    if devices:
        result = Device.devices_schema.dump(devices)
        return jsonify({'message': 'success', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': {}})


def get_device(id):
    device = Device.Device.query.get(id)

    if device:
        return Device.device_schema.jsonify(device)

    return jsonify({'message': 'nothing found', 'data': {}})


def post_device(name, desc, gateway):
    name = name
    desc = desc
    gateway = gateway

    try:
        device = Device.Device(name, desc, gateway)
        db.session.add(device)
        db.session.commit()

        return Device.device_schema.jsonify(device), 201
    except:
        return jsonify({"message": "unable to register device", 'data': {}}), 500


def update_device(id, name, desc, gateway):
    device = Device.Device.query.get(id)
    name = name
    desc = desc
    gateway = gateway

    if device:
        device.name = name
        device.desc = desc
        device.gateway = gateway
        db.session.commit()
        return Device.device_schema.jsonify(device)

    else:
        return jsonify({'message': 'unable to update', 'data': {}})


def delete_device(id):
    device = Device.Device.query.get(id)

    if device:
        db.session.delete(device)
        db.session.commit()
        return Device.device_schema.jsonify(device), 202

    else:
        return jsonify({"message": "unable to register device", 'data': {}}), 404
