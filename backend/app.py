from flask import Flask

from routes.heartbeat import heartbeat_bp

app = Flask(__name__)

app.register_blueprint(
    heartbeat_bp,
    url_prefix="/api/v1"
)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )