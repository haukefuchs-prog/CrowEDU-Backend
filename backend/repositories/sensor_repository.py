from config.database import get_connection


def get_sensor(
    device_id,
    name
):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT sensor_id
        FROM sensors
        WHERE device_id = %s
        AND name = %s
        """,
        (
            device_id,
            name
        )
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def create_sensor(
    device_id,
    name,
    sensor_type_id,
    unit_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO sensors
        (
            device_id,
            name,
            sensor_type_id,
            unit_id,
            active
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            1
        )
        """,
        (
            device_id,
            name,
            sensor_type_id,
            unit_id
        )
    )

    conn.commit()

    sensor_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return sensor_id