from flask import jsonify

from services.device_service import (
    get_device_details
)

def get_device(device_id):

    return jsonify(
        get_device_details(
            device_id
        )
    )