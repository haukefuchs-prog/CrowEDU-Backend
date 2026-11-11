from config.database import get_connection


def update_last_seen(device_name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE devices
        SET last_seen = NOW()
        WHERE name = %s
        """,
        (device_name,)
    )

    conn.commit()

    cursor.close()
    conn.close()