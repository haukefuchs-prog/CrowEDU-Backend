from config.database import get_connection


def get_device_by_serial(
    serial_number
):

    conn = get_connection()
    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM devices
        WHERE serial_number = %s
        """,
        (serial_number,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def get_device_by_id(
    device_id
):

    conn = get_connection()
    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM devices
        WHERE device_id = %s
        """,
        (device_id,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def get_primary_device():

    conn = get_connection()
    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT *
        FROM devices
        LIMIT 1
        """
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def create_device(
    name,
    device_type_id,
    serial_number
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO devices
        (
            location_id,
            name,
            device_type_id,
            serial_number,
            active
        )
        VALUES
        (
            5,
            %s,
            %s,
            %s,
            1
        )
        """,
        (
            name,
            device_type_id,
            serial_number
        )
    )

    conn.commit()

    device_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return device_id


def update_last_seen(
    device_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE devices
        SET last_seen = NOW()
        WHERE device_id = %s
        """,
        (device_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()


def update_device_telemetry(
    device_id,
    node_status,
    network_status,
    backend_status,
    sensor_status,
    fw_version,
    node_uptime_seconds,
    last_reboot
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE devices
        SET
            node_status = %s,
            network_status = %s,
            backend_status = %s,
            sensor_status = %s,
            fw_version = %s,
            node_uptime_seconds = %s,
            last_reboot = %s
        WHERE device_id = %s
        """,
        (
            node_status,
            network_status,
            backend_status,
            sensor_status,
            fw_version,
            node_uptime_seconds,
            last_reboot,
            device_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def update_node_status(
    device_id,
    node_status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE devices
        SET node_status = %s
        WHERE device_id = %s
        """,
        (
            node_status,
            device_id
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_device(device_id):

    conn = get_connection()

    cursor = conn.cursor(
        dictionary=True
    )

    cursor.execute(
        """
        SELECT
            device_id,
            name,
            serial_number,
            node_status,
            network_status,
            backend_status,
            sensor_status,
            fw_version,
            node_uptime_seconds,
            last_reboot,
            last_seen
        FROM devices
        WHERE device_id = %s
        """,
        (device_id,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result