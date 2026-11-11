from config.database import get_connection


def get_device_by_serial(serial_number):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT device_id
        FROM devices
        WHERE serial_number = %s
        """,
        (serial_number,)
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

def update_last_seen(device_id):

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