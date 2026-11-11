from config.database import get_connection


def get_latest_measurements():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            sensor_id,
            ROUND(AVG(value), 2) AS value
        FROM (
            SELECT
                sensor_id,
                value
            FROM measurements
            WHERE sensor_id IN (1, 2)
            ORDER BY measurement_id DESC
            LIMIT 20
        ) recent
        GROUP BY sensor_id
        """
    )

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def get_sensor_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM sensors
        """
    )

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result

def get_node_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM devices
        """
    )

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result

def get_online_node_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM devices
        WHERE last_seen >= DATE_SUB(
            NOW(),
            INTERVAL 2 MINUTE
        )
        """
    )

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result

def get_online_sensor_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM sensors
        WHERE last_seen >= DATE_SUB(
            NOW(),
            INTERVAL 2 MINUTE
        )
        """
    )

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return result