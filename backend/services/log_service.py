from repositories.device_repository import (
    get_device_by_serial
)

from repositories.log_repository import (
    create_log,
    get_warning_level_by_name
)


def create_log_entry(data):

    device = get_device_by_serial(
        data["serial_number"]
    )

    if not device:
        return {
            "success": False,
            "message": "Device not found"
        }

    warning_level = get_warning_level_by_name(
        data["warning_level"]
    )

    if not warning_level:
        return {
            "success": False,
            "message": "Warning level not found"
        }

    log_id = create_log(
        device["device_id"],
        warning_level["warning_level_id"],
        data["message"]
    )

    return {
        "success": True,
        "log_id": log_id
    }