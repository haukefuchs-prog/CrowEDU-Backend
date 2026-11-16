from flask import (
    Blueprint,
    request,
    jsonify
)

from services.telemetry_service import (
    register_telemetry
)

telemetry_bp = Blueprint(
    "telemetry",
    __name__
)


@telemetry_bp.route(
    "/telemetry",
    methods=["POST"]
)
def telemetry():

    data = request.get_json()

    result = register_telemetry(
        data
    )

    return jsonify(
        result
    )