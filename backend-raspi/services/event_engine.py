from services.warning_service import (
    trigger_warning,
    clear_warning
)

from repositories.log_repository import (
    get_online_devices,
    create_log,
    get_warning_level_by_name
)

from repositories.device_repository import (
    update_node_status
)

from datetime import datetime

def process_device_events(
    device,
    telemetry
):

    ensure_node_online(device)

    check_reboot(
        device,
        telemetry
    )

    check_backend_status(
        device,
        telemetry
    )

    check_network_status(
        device,
        telemetry
    )

    check_sensor_status(
        device,
        telemetry
    )

def check_backend_status(
    device,
    telemetry
):
    old_status = device["backend_status"]
    new_status = telemetry["backend_status"]

    if (
        old_status == "connected"
        and new_status == "disconnected"
    ):

        trigger_warning(
            device["device_id"],
            None,
            "WARNING",
            "Backend nicht erreichbar"
        )

    elif (
        old_status == "disconnected"
        and new_status == "connected"
    ):

        clear_warning(
            device["device_id"],
            "Backend nicht erreichbar",
            "Backend wieder erreichbar"
        )

def check_network_status(
    device,
    telemetry
):
    old_status = device["network_status"]
    new_status = telemetry["network_status"]

    if (
        old_status == "connected"
        and new_status == "disconnected"
    ):

        trigger_warning(
            device["device_id"],
            None,
            "WARNING",
            "Netzwerkverbindung verloren"
        )

    elif (
        old_status == "disconnected"
        and new_status == "connected"
    ):

        clear_warning(
            device["device_id"],
            "Netzwerkverbindung verloren",
            "Netzwerkverbindung wiederhergestellt"
        )

def check_offline_devices():
    devices = get_online_devices()

    for device in devices:

        age = (
            datetime.now()
            - device["last_seen"]
        )

        if (
            age.total_seconds() > 180
            and device["node_status"] != "offline"
        ):

            trigger_warning(
                device["device_id"],
                None,
                "ALARM",
                "Node offline"
            )

            update_node_status(
                device["device_id"],
                "offline"
            )

def check_reboot(
    device,
    telemetry
):

    telemetry_reboot = datetime.strptime(
        telemetry["last_reboot"],
        "%Y-%m-%d %H:%M:%S"
    )

    if (
        device["last_reboot"]
        != telemetry_reboot
    ):


        level = get_warning_level_by_name(
            "INFO"
        )

        create_log(
            device["device_id"],
            level["warning_level_id"],
            "Node neu gestartet"
        )

def check_sensor_status(
    device,
    telemetry
):
    old_status = device["sensor_status"]
    new_status = telemetry["sensor_status"]

    if (
        old_status == "online"
        and new_status == "error"
    ):

        trigger_warning(
            device["device_id"],
            None,
            "WARNING",
            "Sensor ausgefallen"
        )

    elif (
        old_status == "error"
        and new_status == "online"
    ):

        clear_warning(
            device["device_id"],
            "Sensor ausgefallen",
            "Sensor wieder verfügbar"
        )

def ensure_node_online(
    device
):

    print(
        "ensure_node_online:",
        device["node_status"]
    )

    if device["node_status"] == "offline":

        clear_warning(
            device["device_id"],
            "Node offline",
            "Node wieder online"
        )

        update_node_status(
            device["device_id"],
            "online"
        )