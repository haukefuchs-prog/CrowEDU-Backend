from config.database import get_connection


def create_measurement(
    sensor_id,
    value
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO measurements
        (
            sensor_id,
            value,
            measured_at
        )
        VALUES
        (
            %s,
            %s,
            NOW()
        )
        """,
        (
            sensor_id,
            value
        )
    )

    cursor.execute(
        """
        UPDATE sensors
        SET last_seen = NOW()
        WHERE sensor_id = %s
        """,
        (sensor_id,)
    )

    conn.commit()

    measurement_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return measurement_id