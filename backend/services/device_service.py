from repositories.device_repository import (
    get_device_by_serial,
    create_device,
    update_last_seen
)

def register_device(data):

    serial_number = data["serial_number"]

    existing = get_device_by_serial(
        serial_number
    )

    if existing:

        update_last_seen(
            existing["device_id"]
        )

        return {
            "success": True,
            "device_id": existing["device_id"]
        }

    device_id = create_device(
        data["name"],
        data["device_type_id"],
        serial_number
    )

    update_last_seen(device_id)

    return {
        "success": True,
        "device_id": device_id
    }