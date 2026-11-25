from services.warning_service import (
    trigger_warning,
    clear_warning
)

def process_measurement_events(
    device,
    measurement
):
    sensor_id = measurement["sensor_id"]

    if sensor_id == 1:

        check_temperature_status(
            device,
            measurement
        )

    elif sensor_id == 2:

        check_humidity_status(
            device,
            measurement
        )

def check_temperature_status(
    device,
    measurement
):
    value = measurement["value"]

    if value > 30:

        trigger_warning(
            device["device_id"],
            measurement["sensor_id"],
            "WARNING",
            "Temperatur zu hoch"
        )

    else:

        clear_warning(
            device["device_id"],
            "Temperatur zu hoch",
            "Temperatur wieder normal"
        )

    if value < 18:

        trigger_warning(
            device["device_id"],
            measurement["sensor_id"],
            "WARNING",
            "Temperatur zu niedrig"
        )

    else:

        clear_warning(
            device["device_id"],
            "Temperatur zu niedrig",
            "Temperatur wieder normal"
        )
def check_humidity_status(
    device,
    measurement
):
    value = measurement["value"]

    if value > 70:

        trigger_warning(
            device["device_id"],
            measurement["sensor_id"],
            "WARNING",
            "Luftfeuchtigkeit zu hoch"
        )

    else:

        clear_warning(
            device["device_id"],
            "Luftfeuchtigkeit zu hoch",
            "Luftfeuchtigkeit wieder normal"
        )

    if value < 30:

        trigger_warning(
            device["device_id"],
            measurement["sensor_id"],
            "WARNING",
            "Luftfeuchtigkeit zu niedrig"
        )

    else:

        clear_warning(
            device["device_id"],
            "Luftfeuchtigkeit zu niedrig",
            "Luftfeuchtigkeit wieder normal"
        )