from repositories.dashboard_repository import (
    get_latest_measurements,
    get_node_count,
    get_online_node_count,
    get_sensor_count,
    get_online_sensor_count,
    get_measurements_last_24h
)

from repositories.device_repository import (
    get_primary_device
)

def get_history():

    return {
        "temperature": get_measurements_last_24h(1),
        "humidity": get_measurements_last_24h(2)
    }

def get_dashboard():

    measurements = get_latest_measurements()
    device = get_primary_device()

    dashboard = {
        "temperature": None,
        "humidity": None,
        "nodes_online": get_online_node_count(),
        "nodes_total": get_node_count(),
        "sensors_online": get_online_sensor_count(),
        "sensors_total": get_sensor_count(),
        "warnings": 0,

        "node_status": device["node_status"],
        "network_status": device["network_status"],
        "backend_status": device["backend_status"],
        "sensor_status": device["sensor_status"],

        "fw_version": device["fw_version"],
        "node_uptime_seconds":
            device["node_uptime_seconds"],
        "last_reboot":
            device["last_reboot"]
    }

    for measurement in measurements:

        if measurement["sensor_id"] == 1:
            dashboard["temperature"] = measurement["value"]

        elif measurement["sensor_id"] == 2:
            dashboard["humidity"] = measurement["value"]

    return dashboard