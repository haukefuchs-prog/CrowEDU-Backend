from repositories.measurement_repository import (
    create_measurement
)


def register_measurement(data):

    measurement_id = create_measurement(
        data["sensor_id"],
        data["value"]
    )

    return {
        "success": True,
        "measurement_id": measurement_id
    }