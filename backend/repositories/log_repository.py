from config.database import get_connection


def create_log(
    device_id,
    warning_level_id,
    message
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO logs
        (
            device_id,
            warning_level_id,
            message,
            created_at
        )
        VALUES
        (
            %s,
            %s,
            %s,
            NOW()
        )
        """,
        (
            device_id,
            warning_level_id,
            message
        )
    )

    conn.commit()

    log_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return log_id

def get_warning_level_by_name(name):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT warning_level_id
        FROM warning_levels
        WHERE name = %s
        """,
        (name,)
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def get_online_devices():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM devices
        WHERE node_status = 'online'
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result