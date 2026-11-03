# CrowEDU Backend

CrowEDU ist ein IoT-basiertes Monitoring- und Lernprojekt zur Überwachung technischer Systeme. Ziel ist die Erfassung, Verarbeitung und Visualisierung von Sensordaten über eine zentrale REST-API.

Dieses Repository enthält das CrowEDU-Backend.

---

# Projektstatus

Aktueller Stand:

- ✅ Datenbankmodell definiert
- ✅ RDS erstellt
- ✅ Datenbankstruktur angelegt
- ✅ Hardwareplattform aufgebaut
- ✅ GPIO-Konzept festgelegt
- ✅ REST-API V1 eingefroren
- ✅ Datenmodell V1 eingefroren
- ✅ Backend-Struktur V1 eingefroren
- 🔲 Backend-Implementierung
- 🔲 Collector-Anbindung
- 🔲 Dashboard-Anbindung
- 🔲 Tests

---

# Systemarchitektur

```text
Raspberry Pi
    ⇅ HTTPS
REST API
    ⇅
MariaDB

Frontend
    ⇅ HTTPS
REST API
```

## Grundsätze

- Keine direkte Verbindung zur MariaDB
- Sämtliche Kommunikation erfolgt über REST
- Frontend dient ausschließlich der Anzeige
- Raspberry Pi arbeitet als Collector und Aktor
- Geschäftslogik liegt ausschließlich im Backend
- Kommunikation erfolgt über HTTPS

---

# Repository-Struktur

```text
crowedu-backend/
│
├── app.py
├── requirements.txt
├── README.md
│
├── config/
├── routes/
├── services/
├── repositories/
├── models/
├── utils/
├── tests/
└── docs/
```

Details zur Struktur befinden sich in:

```text
docs/folder-structure-freeze-v1.md
```

---

# Dokumentation

Die zentrale Projektdokumentation befindet sich im Ordner:

```text
docs/
```

Verfügbare Dokumente:

```text
architecture.md
folder-structure-freeze-v1.md
api-freeze-v1.md
data-model-freeze-v1.md
roadmap.md
```

Vor Beginn der Entwicklung sollten diese Dokumente gelesen werden.

---

# Architektur-Freeze

Für CrowEDU V1 wurden folgende Bereiche eingefroren:

- Architektur
- Datenmodell
- API-Struktur
- GPIO-Belegung
- Backend-Struktur

Änderungen an diesen Bereichen erfolgen ausschließlich durch bewusste Architekturentscheidungen.

---

# API-Version

Aktuelle Version:

```text
/api/v1/
```

Beispiele:

```text
/api/v1/dashboard
/api/v1/measurements
/api/v1/warnings
/api/v1/logs
```

---

# Entwicklungsrichtlinien

## Routes

Verantwortlich für:

- Requests entgegennehmen
- Responses zurückgeben

Keine Geschäftslogik.

---

## Services

Verantwortlich für:

- Grenzwertprüfung
- Warnungslogik
- Dashboarddaten
- Gerätezustände

Hier liegt die gesamte Geschäftslogik.

---

## Repositories

Verantwortlich für:

- Datenbankzugriffe
- SELECT
- INSERT
- UPDATE
- DELETE

Keine Geschäftslogik.

---

## Models

Verantwortlich für:

- Datenstrukturen
- Datenobjekte
- Validierung

---

# Mitwirken

Vor Entwicklungsbeginn:

1. Dokumentation lesen
2. Architektur-Freeze beachten
3. API-Freeze beachten
4. Data-Model-Freeze beachten

Neue Funktionen sollen nach Möglichkeit innerhalb der bestehenden Architektur umgesetzt werden.

---

# Ziel von CrowEDU

CrowEDU soll als Lern- und Monitoringplattform dienen, die technische Systeme über Sensorik überwacht, Messwerte zentral verarbeitet und Ergebnisse über Dashboard sowie Statusanzeigen visualisiert.

Im Mittelpunkt stehen:

- IoT
- Datenbanken
- REST-APIs
- Linux
- Raspberry Pi
- Monitoring
- Softwareentwicklung
- Dokumentation

---

# Lizenz

Aktuell nicht festgelegt.
