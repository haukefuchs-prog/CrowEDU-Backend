from flask import Flask
from flask_cors import CORS

from routes.heartbeat import heartbeat_bp
from routes.devices import devices_bp
from routes.sensors import sensors_bp
from routes.measurements import measurements_bp
from routes.dashboard import dashboard_bp
from routes.node_heartbeat import (
    node_heartbeat_bp
)
from routes.logs import logs_bp
from routes.telemetry import (
    telemetry_bp
)

import threading
import time

from services.event_engine import (
    check_offline_devices
)

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    heartbeat_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    devices_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    sensors_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    measurements_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    dashboard_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    node_heartbeat_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    logs_bp,
    url_prefix="/api/v1"
)

app.register_blueprint(
    telemetry_bp,
    url_prefix="/api/v1"
)

def event_loop():

    while True:

        try:

            check_offline_devices()

        except Exception as e:

            print(
                f"Event Engine Fehler: {e}"
            )

        time.sleep(60)

if __name__ == "__main__":

    threading.Thread(
        target=event_loop,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )