crowedu-backend/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── config.py
│   └── database.py
│
├── routes/
│   ├── dashboard.py
│   ├── devices.py
│   ├── sensors.py
│   ├── measurements.py
│   ├── warnings.py
│   ├── logs.py
│   └── heartbeat.py
│
├── services/
│   ├── dashboard_service.py
│   ├── device_service.py
│   ├── sensor_service.py
│   ├── measurement_service.py
│   ├── warning_service.py
│   ├── log_service.py
│   └── heartbeat_service.py
│
├── repositories/
│   ├── device_repository.py
│   ├── sensor_repository.py
│   ├── measurement_repository.py
│   ├── warning_repository.py
│   └── log_repository.py
│
├── models/
│   ├── device.py
│   ├── sensor.py
│   ├── measurement.py
│   ├── warning.py
│   └── log.py
│
├── utils/
│   ├── response.py
│   ├── validation.py
│   └── logger.py
│
├── tests/
│   ├── test_devices.py
│   ├── test_sensors.py
│   ├── test_measurements.py
│   ├── test_warnings.py
│   └── test_logs.py
│
└── docs/
    ├── api.md
    ├── architecture.md
    └── roadmap.md