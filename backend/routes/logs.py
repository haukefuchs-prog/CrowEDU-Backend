from flask import Blueprint
from flask import request

from services.log_service import (
    create_log_entry
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