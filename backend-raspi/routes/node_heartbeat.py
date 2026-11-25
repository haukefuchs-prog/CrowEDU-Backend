from flask import Blueprint
from flask import request

from services.node_heartbeat_service import (
    process_heartbeat
)

node_heartbeat_bp = Blueprint(
    "node_heartbeat",
    __name__
)


@node_heartbeat_bp.route(
    "/heartbeat",
    methods=["POST"]
)
def heartbeat():

    data = request.get_json()

    return process_heartbeat(
        data["device_name"]
    )
