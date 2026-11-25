from flask import Blueprint

from services.warning_service import (
    get_warnings
)

warnings_bp = Blueprint(
    "warnings",
    __name__
)

@warnings_bp.route(
    "/warnings",
    methods=["GET"]
)
def get_warnings_route():

    return get_warnings()