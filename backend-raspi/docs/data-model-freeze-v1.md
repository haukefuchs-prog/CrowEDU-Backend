# CrowEDU Data Model Freeze V1

Status: EINGEFROREN
Version: 1.0

Zweck:
Dieses Dokument definiert die fachlichen Datenobjekte
des CrowEDU-Systems. Änderungen an diesen Modellen
dürfen nur durch eine bewusste Architekturentscheidung
erfolgen.

==================================================
1. DEVICE
==================================================

Beschreibung:

Ein Device repräsentiert ein physisches System,
welches Messwerte erfasst und mit dem Backend
kommuniziert.

Beispiel:

- Raspberry Pi
- Sensor-Node
- Monitoring-System

Attribute:

id
location_id
device_type_id
name
hostname
status
created_at

JSON-Beispiel:

{
    "id": 1,
    "location_id": 1,
    "device_type_id": 1,
    "name": "CrowEDU Node 01",
    "hostname": "crowedu-node-01",
    "status": "online",
    "created_at": "2026-11-03 18:00:00"
}

==================================================
2. SENSOR
==================================================

Beschreibung:

Ein Sensor ist einem Device zugeordnet und liefert
Messwerte.

Attribute:

id
device_id
sensor_type_id
name
gpio
status

JSON-Beispiel:

{
    "id": 1,
    "device_id": 1,
    "sensor_type_id": 1,
    "name": "Temperatur",
    "gpio": 24,
    "status": "online"
}

==================================================
3. MEASUREMENT
==================================================

Beschreibung:

Ein Measurement stellt einen einzelnen Messwert
eines Sensors dar.

Attribute:

id
sensor_id
value
measured_at

JSON-Beispiel:

{
    "id": 1024,
    "sensor_id": 1,
    "value": 22.8,
    "measured_at": "2026-11-03 18:30:00"
}

==================================================
4. WARNING
==================================================

Beschreibung:

Warnungen werden vom Backend erzeugt, sobald
definierte Grenzwerte überschritten oder Fehler
erkannt werden.

Attribute:

id
sensor_id
warning_level_id
message
active
created_at

JSON-Beispiel:

{
    "id": 10,
    "sensor_id": 1,
    "warning_level_id": 2,
    "message": "Temperatur erhöht",
    "active": true,
    "created_at": "2026-11-03 18:31:00"
}

==================================================
5. LOG
==================================================

Beschreibung:

Logs dokumentieren Systemereignisse und
Statusinformationen.

Attribute:

id
device_id
level
message
created_at

JSON-Beispiel:

{
    "id": 55,
    "device_id": 1,
    "level": "INFO",
    "message": "Heartbeat received",
    "created_at": "2026-11-03 18:32:00"
}

==================================================
6. BEZIEHUNGEN
==================================================

Location
└── Devices

DeviceType
└── Devices

Device
└── Sensors

SensorType
└── Sensors

Sensor
└── Measurements

Sensor
└── Warnings

WarningLevel
└── Warnings

Device
└── Logs

==================================================
7. STATUSWERTE
==================================================

Device Status:

online
offline
warning
error

--------------------------------------------------

Sensor Status:

online
offline
warning
error

--------------------------------------------------

Log Level:

INFO
WARNING
ERROR

==================================================
8. BACKEND-VERANTWORTUNG
==================================================

Das Backend erzeugt:

- Warnings
- Statuswerte
- Dashboarddaten
- Historien
- Signalfarben

Sensoren liefern ausschließlich Messwerte.

==================================================
9. V1-GRENZEN
==================================================

Nicht Bestandteil des Datenmodells V1:

- Benutzer
- Rollen
- Rechte
- API-Schlüssel
- Benachrichtigungen
- Mobile Clients
- MQTT-Geräte

==================================================
10. FREEZE-BESCHLUSS
==================================================

[✓] Device Modell eingefroren

[✓] Sensor Modell eingefroren

[✓] Measurement Modell eingefroren

[✓] Warning Modell eingefroren

[✓] Log Modell eingefroren

[✓] Beziehungen definiert

[✓] Statuswerte definiert

Änderungen nur durch bewusste
Architekturentscheidung und Versionswechsel.