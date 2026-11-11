from repositories.dashboard_repository import (
    get_latest_measurements,
    get_node_count,
    get_online_node_count,
    get_sensor_count,
    get_online_sensor_count
)


def get_dashboard():

    measurements = get_latest_measurements()

    dashboard = {
        "temperature": None,
        "humidity": None,
        "nodes_online": get_online_node_count(),
        "nodes_total": get_node_count(),
        "sensors_online": get_online_sensor_count(),
        "sensors_total": get_sensor_count(),
        "warnings": 0
    }

    for measurement in measurements:

        if measurement["sensor_id"] == 1:
            dashboard["temperature"] = measurement["value"]

        elif measurement["sensor_id"] == 2:
            dashboard["humidity"] = measurement["value"]

    return dashboard