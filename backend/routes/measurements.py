from flask import Blueprint, request, jsonify

from services.measurement_service import (
    register_measurement
)

measurements_bp = Blueprint(
    "measurements",
    __name__
)

@measurements_bp.route(
    "/measurements",
    methods=["POST"]
)
def measurement_register():

    data = request.get_json()

    result = register_measurement(data)

    return jsonify(result)
