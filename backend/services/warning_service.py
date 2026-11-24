from repositories.log_repository import (
    create_log,
    get_warning_level_by_name
)

from repositories.warning_repository import (
    create_warning,
    get_active_warning,
    resolve_warning,
    get_active_warnings
)

def get_warnings():
    return get_active_warnings()

def trigger_warning(
    device_id,
    sensor_id,
    level_name,
    message
):

    print(f"WARNING: {message}")

    active_warning = get_active_warning(
        device_id,
        message
    )

    print("active_warning =", active_warning)

    if active_warning:
        print("WARNING existiert bereits")
        return False

    level = get_warning_level_by_name(
        level_name
    )

    print("level =", level)

    create_log(
        device_id,
        level["warning_level_id"],
        message
    )

    print("log geschrieben")

    create_warning(
        device_id,
        sensor_id,
        level["warning_level_id"],
        message
    )

    print("warning geschrieben")

    return True


def clear_warning(
    device_id,
    warning_message,
    resolved_message
):
    active_warning = get_active_warning(
        device_id,
        warning_message
    )

    if not active_warning:
        return False

    resolve_warning(
        active_warning["warning_id"]
    )

    level = get_warning_level_by_name(
        "INFO"
    )

    create_log(
        device_id,
        level["warning_level_id"],
        resolved_message
    )

    return True