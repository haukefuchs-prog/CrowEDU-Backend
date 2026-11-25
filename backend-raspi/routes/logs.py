from flask import Blueprint
from flask import request

from services.log_service import (
    create_log_entry,
    get_logs
)

logs_bp = Blueprint(
    "logs",
    __name__
)


@logs_bp.route(
    "/logs",
    methods=["POST"]
)
def log():

    data = request.get_json()

    return create_log_entry(data)

@logs_bp.route(
    "/logs",
    methods=["GET"]
)
def get_logs_route():

    return get_logs()