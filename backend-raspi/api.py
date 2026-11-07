from flask import Flask, Response
from sensors.sht31 import read_sensor

from datetime import datetime
from zoneinfo import ZoneInfo

import socket
import subprocess

app = Flask(__name__)

FW_VERSION = "1.0.0"

BOOT_TIME = datetime.now(
    ZoneInfo("Europe/Berlin")
)

LAST_REBOOT = BOOT_TIME.isoformat()


def get_uptime_seconds():
    return int(
        (
            datetime.now(
                ZoneInfo("Europe/Berlin")
            ) - BOOT_TIME
        ).total_seconds()
    )


def get_wifi_rssi():
    try:
        result = subprocess.check_output(
            [
                "bash",
                "-c",
                "iwconfig wlan0 | grep 'Signal level'"
            ],
            text=True
        )

        return int(
            result.split("Signal level=")[1]
            .split(" ")[0]
        )

    except Exception:
        return -999


@app.route("/metrics")
def metrics():

    try:
        temperature, humidity = read_sensor()

        timestamp = datetime.now(
            ZoneInfo("Europe/Berlin")
        ).isoformat()

        data = f"""temperature_celsius {round(temperature, 2)}
humidity_percent {round(humidity, 2)}
node_name "{socket.gethostname()}"
fw_version "{FW_VERSION}"
node_uptime_seconds {get_uptime_seconds()}
wifi_rssi {get_wifi_rssi()}
last_reboot "{LAST_REBOOT}"
timestamp "{timestamp}"
"""

        return Response(
            data,
            mimetype="text/plain"
        )

    except Exception as e:

        timestamp = datetime.now(
            ZoneInfo("Europe/Berlin")
        ).isoformat()

        data = f"""node_name "{socket.gethostname()}"
fw_version "{FW_VERSION}"
error "{str(e)}"
timestamp "{timestamp}"
"""

        return Response(
            data,
            status=500,
            mimetype="text/plain"
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )