# CrowEDU API Freeze V1

Status: EINGEFROREN

Version: 1.0

Gültig ab: Architektur-Freeze V1

---

# 1. Zweck

Die CrowEDU REST-API bildet die zentrale Kommunikations-
schnittstelle zwischen:

- Raspberry Pi (Datenerfassung und Aktorik)
- Backend
- Frontend
- MariaDB

Direkte Datenbankzugriffe durch Clients sind nicht erlaubt.

Sämtliche Kommunikation erfolgt über HTTPS und die REST-API.

---

# 2. Systemarchitektur

Raspberry Pi
    ⇅ HTTPS
REST API
    ⇅
MariaDB

Frontend
    ⇅ HTTPS
REST API

Regeln:

- Raspberry liest und schreibt ausschließlich über die API.
- Das Frontend greift ausschließlich über die API auf Daten zu.
- Das Backend beinhaltet die Geschäftslogik.
- MariaDB wird niemals direkt von Clients angesprochen.
- NAT- und Firewall-Netze werden unterstützt.

---

# 3. API-Versionierung

Alle Endpunkte beginnen mit:

/api/v1/

Beispiele:

/api/v1/health
/api/v1/heartbeat
/api/v1/measurements

---

# 4. Unterstützte Datentypen

Messwerte

- Temperatur
- Luftfeuchtigkeit

Systeminformationen

- Heartbeat
- Verbindungsstatus
- Firmware-Version
- Uptime

---

# 5. Freigegebene Endpunkte V1

## Health Check

GET /api/v1/health

Zweck:

- Backend-Erreichbarkeit prüfen
- API-Version ermitteln
- Serverstatus abrufen

---

## Heartbeat

POST /api/v1/heartbeat

Zweck:

- Online-Status eines Gerätes melden
- Letzten Kontakt speichern
- Uptime übertragen

---

## Measurements

POST /api/v1/measurements

Zweck:

- Temperatur speichern
- Luftfeuchtigkeit speichern
- Zeitstempel übertragen

---

# 6. Antwortformat

Antworten werden ausschließlich als JSON übertragen.

Beispiel:

{
  "success": true,
  "message": "Measurement stored"
}

---

# 7. Authentifizierung

Wird in Version 1 vorbereitet.

Authentifizierung über API-Key vorgesehen.

---

# 8. Änderungsregel

Dieses Dokument gilt als eingefroren.

Neue API-Endpunkte werden nicht in dieses Dokument
aufgenommen.

Erweiterungen werden zunächst in der API-Roadmap
diskutiert und nach Umsetzung in einem späteren
API-Freeze dokumentiert.

Version 1.0 ist abgeschlossen.
