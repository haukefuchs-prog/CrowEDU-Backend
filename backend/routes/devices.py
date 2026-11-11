from flask import Blueprint, request, jsonify

from services.device_service import register_device

devices_bp = Blueprint(
    "devices",
    __name__
)

@devices_bp.route(
    "/devices/register",
    methods=["POST"]
)
def device_register():

    data = request.get_json()

    result = register_device(data)

    return jsonify(result)
