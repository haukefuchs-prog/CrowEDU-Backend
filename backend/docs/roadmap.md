# CrowEDU API Roadmap V1 (Freeze)

Status: ARCHITEKTUR-FREEZE V1

==================================================
1. SYSTEMARCHITEKTUR
==================================================

Raspberry Pi
    ⇅ HTTPS
REST API
    ⇅
MariaDB

Frontend
    ⇅ HTTPS
REST API


Grundsätze:

- Keine direkte Verbindung zur MariaDB
- Raspberry Pi kommuniziert ausschließlich per REST API
- Frontend kommuniziert ausschließlich per REST API
- Frontend dient ausschließlich der Anzeige
- Sämtliche Geschäftslogik liegt im Backend
- Raspberry befindet sich in einem NAT-/Firewall-Netzwerk
- Raspberry kann nur ausgehende HTTPS-Verbindungen initiieren
- Eingehende Verbindungen zum Raspberry werden nicht unterstützt

==================================================
2. API-VERSIONIERUNG
==================================================

Basis:

/api/v1/

Beispiele:

/api/v1/measurements
/api/v1/warnings
/api/v1/logs

==================================================
3. OBJEKTE DER API
==================================================

Locations
Devices
DeviceTypes
Sensors
SensorTypes
Units
Measurements
WarningLevels
Warnings
Logs

==================================================
4. RASPBERRY -> BACKEND
==================================================

Heartbeat senden

POST /api/v1/heartbeat

--------------------------------------------------

Messwert senden

POST /api/v1/measurements

Beispiel:

{
    "device_id": 1,
    "sensor_id": 1,
    "value": 22.8
}

--------------------------------------------------

Logeintrag senden

POST /api/v1/logs

Beispiel:

{
    "device_id": 1,
    "level": "INFO",
    "message": "Measurement received"
}

==================================================
5. RASPBERRY <- BACKEND
==================================================

Gerätestatus abrufen

GET /api/v1/device-state/{device_id}

Beispiel:

{
    "status": "online",
    "signal": "green"
}

--------------------------------------------------

Aktive Warnungen abrufen

GET /api/v1/warnings/active/{device_id}

==================================================
6. FRONTEND -> BACKEND
==================================================

Dashboarddaten

GET /api/v1/dashboard

Liefert:

- aktuelle Temperatur
- aktuelle Luftfeuchtigkeit
- Sensorstatus
- Anzahl Warnungen

--------------------------------------------------

Messwerte aktuell

GET /api/v1/measurements/latest

--------------------------------------------------

Messwert-Historie

GET /api/v1/measurements/history

Parameter:

?hours=24
?days=7
?days=30

--------------------------------------------------

Warnungen

GET /api/v1/warnings

--------------------------------------------------

Logs

GET /api/v1/logs

--------------------------------------------------

Sensoren

GET /api/v1/sensors

--------------------------------------------------

Geräte

GET /api/v1/devices

==================================================
7. BACKEND-VERANTWORTUNG
==================================================

Das Backend entscheidet:

- Warnungen erzeugen
- Grenzwerte überwachen
- Gerätezustand bestimmen
- Statusfarbe bestimmen
- Historie speichern
- Logs speichern

Der Raspberry bewertet keine Messwerte.

Beispiel:

Temperatur = 31°C

Backend:
-> Warnung erzeugen
-> Signal = yellow

Antwort:

{
    "signal": "yellow"
}

==================================================
8. GPIO-FREEZE
==================================================

GPIO17 = Grün
GPIO27 = Gelb
GPIO22 = Rot
GPIO23 = Blau

GPIO24 = Temperatursensor

Weiß:
Direkt mit 12V verbunden.
Nicht softwaregesteuert.

==================================================
9. DASHBOARD-KOMPONENTEN
==================================================

Dashboard Übersicht

- Temperatur
- Luftfeuchtigkeit
- Sensorstatus
- Warnungen

--------------------------------------------------

Diagramme

- Temperaturverlauf
- Luftfeuchtigkeitsverlauf

--------------------------------------------------

Ereignisse

- Aktive Warnungen
- Historie
- Logs

==================================================
10. NICHT BESTANDTEIL VON V1
==================================================

- MQTT
- Benutzerverwaltung
- Rollenmodell
- Mobile App
- Push-Benachrichtigungen
- WebSockets
- KI-Auswertung

==================================================
11. ENTSCHEIDUNGEN (EINGEFROREN)
==================================================

[✓] REST API als zentrale Schnittstelle
[✓] MariaDB niemals direkt erreichbar
[✓] Frontend ist Read-Only
[✓] Backend enthält Geschäftslogik
[✓] Raspberry arbeitet als Collector/Aktor
[✓] HTTPS als Kommunikationsweg
[✓] API-Versionierung mit /api/v1/