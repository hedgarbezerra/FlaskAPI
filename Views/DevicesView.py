from flask import jsonify, request
from sqlalchemy import or_
from Models import Device
from app import db


def get_devices(current_user):
    gateway = request.args.get('gateway')
    name = request.args.get('name')
    type = request.args.get('type')
    limit = request.args.get('limit')
    if gateway or name or type:
        if limit:
            devices = Device.Devices.query.filter(Device.Devices.user_id == current_user.id, or_(Device.Devices.name == name,
                                                                                   Device.Devices.type == type,
                                                                                   Device.Devices.gateway == gateway)).order_by(
                Device.Devices.created_at.desc()).limit(limit)
        else:
            devices = Device.Devices.query.filter(Device.Devices.user_id == current_user.id, or_(Device.Devices.name == name,
                                                                                   Device.Devices.type == type,
                                                                                   Device.Devices.gateway == gateway)).order_by(
                Device.Devices.created_at.desc())
    else:
        devices = Device.Devices.query.filter(Device.Devices.user_id == current_user.id).order_by(Device.Devices.created_at.desc())

    if devices:
        result = Device.devices_schema.dump(devices)
        return jsonify({'message': 'fetched successfully', 'data': result.data})

    return jsonify({'message': 'nothing found', 'data': []})


def get_device(current_user, id):
    try:
        device = Device.Devices.query.filter(Device.Devices.user_id == current_user.id, Device.Devices.id == id).one()
        result = Device.device_schema.jsonify(device)
        return jsonify({'message': 'fetched successfully', 'data': result.data})
    except:
        return jsonify({'message': 'nothing found', 'data': []})


def post_device(name, type, gateway, current_user):
    try:
        device = Device.Devices(name, type, gateway, current_user.id)
        db.session.add(device)
        db.session.commit()

        return Device.device_schema.jsonify(device), 201
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
