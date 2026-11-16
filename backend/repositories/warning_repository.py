from config.database import get_connection


def create_warning(
    device_id,
    sensor_id,
    warning_level_id,
    message
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warnings
        (
            device_id,
            sensor_id,
            warning_level_id,
            message,
            triggered_at,
            active
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            NOW(),
            1
        )
        """,
        (
            device_id,
            sensor_id,
            warning_level_id,
            message
        )
    )

    conn.commit()

    warning_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return warning_id


def get_active_warning(
    device_id,
    message
):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT warning_id
        FROM warnings
        WHERE device_id = %s
        AND message = %s
        AND active = 1
        LIMIT 1
        """,
        (
            device_id,
            message
        )
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def resolve_warning(
    warning_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE warnings
        SET
            active = 0,
            resolved_at = NOW()
        WHERE warning_id = %s
        """,
        (warning_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()