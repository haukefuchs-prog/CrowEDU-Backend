from sqlite3.dbapi2 import Timestamp
from flask import Flask, Response
from sensors.sht31 import read_sensor
from leds.led_controller import (
    green_on,
    red_on,
    yellow_on,
    blue_on,
    all_off
)

import time
import requests
import threading

import leds.led_controller as leds
from datetime import datetime, timezone, timedelta
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



def boot_test():
    """LED-Test beim Einschalten"""

    all_off()

    red_on()
    time.sleep(0.5)

    yellow_on()
    time.sleep(0.5)

    green_on()
    time.sleep(0.5)

    blue_on()
    time.sleep(0.5)

    all_off()


def network_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


def backend_available():
    try:
        response = requests.get(
            "https://api.crowedu.de/api/v1/health",
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("status") == "ok"

        return False

    except Exception:
        return False


def set_red():
    all_off()
    red_on()


def set_red_blue():
    all_off()
    red_on()
    blue_on()


def set_green_blue():
    all_off()
    green_on()
    blue_on()


def wait_for_network():
    """Rot + blinkendes Blau"""

    red_on()

    state = False

    while not network_available():

        if state:
            blue_on()
        else:
            all_off()
            red_on()

        state = not state
        time.sleep(0.5)

    set_red_blue()


def wait_for_backend():
    """Rot + Blau bis Backend OK"""

    set_red_blue()

    while not backend_available():
        time.sleep(2)

    set_green_blue()

def state_network_lost():
    all_off()
    red_on()

def state_backend_lost():
    all_off()
    red_on()
    blue_on()

def state_online():
    all_off()
    green_on()
    blue_on()

def monitor_loop():

    blink_state = False

    while True:

        if not network_available():

            if blink_state:
                all_off()
                red_on()
                blue_on()
            else:
                all_off()
                red_on()

            blink_state = not blink_state

        elif not backend_available():

            state_backend_lost()

        else:

            state_online()

        time.sleep(1)


if __name__ == "__main__":

    print("CrowEDU Boot Sequence")

    boot_test()

    print("Waiting for network...")
    wait_for_network()

    print("Waiting for backend...")
    wait_for_backend()

    print("Node online.")

    threading.Thread(
        target=monitor_loop,
        daemon=True
    ).start()

    app.run(host="0.0.0.0", port=5000)