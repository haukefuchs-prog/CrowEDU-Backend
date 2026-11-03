# CrowEDU API Freeze Dokument V1

Status: EINGEFROREN
Version: 1.0
Gültig ab: Architektur-Freeze V1

==================================================
1. ZWECK
==================================================

Die CrowEDU REST-API bildet die zentrale
Kommunikationsschnittstelle zwischen:

- Raspberry Pi (Collector + Aktor)
- Backend
- MariaDB
- Frontend

Direkte Datenbankzugriffe sind nicht erlaubt.

Sämtliche Kommunikation erfolgt über HTTPS
und die REST-API.

==================================================
2. SYSTEMARCHITEKTUR
==================================================

Raspberry Pi
    ⇅ HTTPS
REST API
    ⇅
MariaDB

Frontend
    ⇅ HTTPS
REST API

Regeln:

[✓] Raspberry liest und schreibt über API
[✓] Frontend liest ausschließlich über API
[✓] Backend enthält die Geschäftslogik
[✓] MariaDB wird niemals direkt angesprochen
[✓] NAT-/Firewall-Netze werden unterstützt

==================================================
3. API-VERSIONIERUNG
==================================================

Alle Endpunkte beginnen mit:

/api/v1/

Beispiele:

/api/v1/dashboard
/api/v1/measurements
/api/v1/warnings

==================================================
4. RASPBERRY -> BACKEND
==================================================

--------------------------------------------------
Heartbeat senden
--------------------------------------------------

POST /api/v1/heartbeat

Zweck:

- Gerät online melden
- Letzte Kommunikation speichern

--------------------------------------------------
Messwerte senden
--------------------------------------------------

POST /api/v1/measurements

