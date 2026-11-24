from repositories.device_repository import (
    get_device_by_serial,
    update_device_telemetry
)

from services.event_engine import (
    process_device_events
)

from repositories.log_repository import (
    create_log,
    get_warning_level_by_name
)

from repositories.warning_repository import (
    has_active_warnings
)

def register_telemetry(data):

    device = get_device_by_serial(
        data["serial_number"]
    )

    if not device:

        return {
            "success": False,
            "message": "Device not found"
        }

    process_device_events(
        device,
        data
    )

    update_device_telemetry(
        device["device_id"],
        data["node_status"],
        data["network_status"],
        data["backend_status"],
        data["sensor_status"],
        data["fw_version"],
        data["node_uptime_seconds"],
        data["last_reboot"]
    )

    return {
        "success": True,
        "warning_active": has_active_warnings(
            device["device_id"]
        )
    }