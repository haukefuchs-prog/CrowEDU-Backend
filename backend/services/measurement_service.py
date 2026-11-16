from repositories.measurement_repository import (
    create_measurement
)

from services.measurement_event_engine import (
    process_measurement_events
)

from repositories.sensor_repository import (
    get_sensor_by_id
)

from repositories.device_repository import (
    get_device_by_id
)

def register_measurement(data):

    measurement_id = create_measurement(
        data["sensor_id"],
        data["value"]
    )

    sensor = get_sensor_by_id(
        data["sensor_id"]
    )

    device = get_device_by_id(
        sensor["device_id"]
    )

    process_measurement_events(
        device,
        data
    )

    return {
        "success": True,
        "measurement_id": measurement_id
    }