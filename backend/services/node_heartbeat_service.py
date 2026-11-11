from flask import jsonify

from repositories.node_heartbeat_repository import (
    update_last_seen
)


def process_heartbeat(device_name):

    update_last_seen(device_name)

    return jsonify({
        "success": True,
        "device_name": device_name
    })