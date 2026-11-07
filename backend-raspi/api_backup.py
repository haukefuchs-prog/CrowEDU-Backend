from sqlite3.dbapi2 import Timestamp
from flask import Flask, jsonify
from sensors.sht31 import read_sensor
from leds.led_controller import (
    green_on,
    red_on,
    yellow_on,
    blue_on,
    all_off
)

import leds.led_controller as leds
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

import socket

lastreboot = datetime.now(
    ZoneInfo("Europe/Berlin")
    ).isoformat()


app = Flask(__name__)
app.json.sort_keys = False

@app.route("/heartbeat")
def health():
    return {"heartbeat":"OK"}

@app.route("/info")
def info():
    return jsonify({
        "node": socket.gethostname(),
        "version": "0.1.0",
        "hardware": "Raspberry Pi",
        "sensor": "SHT31",
        "api": "CrowEDU",
        "status": "online",
        "last_reboot":lastreboot
    })


@app.route("/metrics")
def metrics():
    try:
        temperature, humidity = read_sensor()
        timestamp = datetime.now(
            ZoneInfo("Europe/Berlin")
            ).isoformat()

        return jsonify({
            "node": socket.gethostname(),
            "status": "online",
            "timestamp": timestamp,
            "temperature": round(temperature, 2),
            "humidity": round(humidity, 2)
        })

    except Exception as e:
        return jsonify({
            "node": socket.gethostname(),
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/leds/green/on")
def green_on_route():
    green_on()
    return {"status": "green on"}

@app.route("/leds/yellow/on")
def yellow_on_route():
    yellow_on()
    return {"status": "yellow on"}

@app.route("/leds/red/on")
def red_on_route():
    red_on()
    return {"status": "red on"}

@app.route("/leds/blue/on")
def blue_on_route():
    blue_on()
    return {"status": "blue on"}

@app.route("/leds/all/off")
def all_off_route():
    all_off()
    return {"status": "all off"}

@app.route("/leds/status")
def led_status():
    return jsonify({
        "active_led": leds.current_led
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)