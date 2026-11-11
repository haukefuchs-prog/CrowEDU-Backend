from flask import Blueprint, request, jsonify

from services.sensor_service import register_sensor

sensors_bp = Blueprint(
    "sensors",
    __name__
)

@sensors_bp.route(
    "/sensors/register",
    methods=["POST"]
)
def sensor_register():

    data = request.get_json()

    result = register_sensor(data)

    return jsonify(result)