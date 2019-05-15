from flask import jsonify, request
from sqlalchemy import or_
from Models import Device
from app import db


def get_devices():
    gateway = request.args.get('gateway')
    name = request.args.get('name')
    type = request.args.get('type')
    if gateway or name or type:
        devices = Device.Devices.query.filter(or_(Device.Devices.name == name, Device.Devices.type == type, Device.Devices.gateway == gateway))
    else:
        devices = Device.Devices.query.all()
    if devices:
        result = Device.devices_schema.dump(devices)
        return jsonify({'message': 'fetched successfully', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': []})


def get_device(id):
    device = Device.Device.query.get(id)

    if device:
        return jsonify({'message': 'nothing found', 'data': Device.device_schema.jsonify(device)})

    return jsonify({'message': 'nothing found', 'data': []})


def post_device(name, type, gateway):
    name = name
    type = type
    gateway = gateway

    try:
        device = Device.Device(name, type, gateway)
        db.session.add(device)
        db.session.commit()

        return jsonify({'message': 'successfully fetched', 'data': Device.device_schema.jsonify(device)}), 201
    except:
        return jsonify({"message": "unable to register device", 'data': []}), 500


def update_device(id, name, type, gateway):
    device = Device.Device.query.get(id)
    name = name
    type = type
    gateway = gateway

    if device:
        device.name = name
        device.type = type
        device.gateway = gateway
        db.session.commit()
        return jsonify({'message': 'successfully fetched', 'data': Device.device_schema.jsonify(device)})

    else:
        return jsonify({'message': 'unable to update', 'data': []})


def delete_device(id):
    device = Device.Device.query.get(id)

    if device:
        db.session.delete(device)
        db.session.commit()
        return jsonify({'message': 'successfully fetched', 'data': Device.device_schema.jsonify(device)}), 202

    else:
        return jsonify({"message": "unable to register device", 'data': []}), 404
