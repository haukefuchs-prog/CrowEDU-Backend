from repositories.sensor_repository import (
    get_sensor,
    create_sensor
)

def register_sensor(data):

    existing = get_sensor(
        data["device_id"],
        data["name"]
    )

    if existing:

        return {
            "success": True,
            "sensor_id": existing["sensor_id"]
        }

    sensor_id = create_sensor(
        data["device_id"],
        data["name"],
        data["sensor_type_id"],
        data["unit_id"]
    )

    return {
        "success": True,
        "sensor_id": sensor_id
    }