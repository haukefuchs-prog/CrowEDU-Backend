from flask import Blueprint, request, jsonify

from services.device_service import (
    register_device,
    get_device_details
)

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


@devices_bp.route(
    "/devices/<int:device_id>",
    methods=["GET"]
)
def device_details(device_id):

    result = get_device_details(
        device_id
    )

    return jsonify(result)