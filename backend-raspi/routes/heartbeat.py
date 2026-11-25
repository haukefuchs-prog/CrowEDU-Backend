from flask import Blueprint

from services.heartbeat_service import get_status

heartbeat_bp = Blueprint(
    "heartbeat",
    __name__
)

@heartbeat_bp.route(
    "/health",
    methods=["GET"]
)
def health():
    return get_status()