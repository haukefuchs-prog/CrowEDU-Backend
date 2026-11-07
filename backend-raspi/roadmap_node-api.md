# CrowEDU Node API Freeze V1

Status: EINGEFROREN

Version: 1.0

Gültig ab: Node Freeze V1

---

# 1. Zweck

Die Node API stellt Messwerte und Systeminformationen
eines CrowEDU Nodes für externe Systeme bereit.

Die API ist backendunabhängig.

Sie kann von CrowEDU sowie von Drittanwendungen
genutzt werden.

Beispiele:

- CrowEDU Backend
- Grafana
- Prometheus
- PRTG
- Home Assistant
- Node-RED

---

# 2. Architektur

CrowEDU Node
      ↓
   /metrics
      ↓
 Beliebige Clients

Der Node ist nicht an ein bestimmtes Backend gebunden.

---

# 3. API-Version

Version: 1.0

Node-Endpunkte:

GET /metrics

---

# 4. Content-Type

Die Antwort wird als Text ausgeliefert.

Beispiel:

temperature_celsius 17.36
humidity_percent 57.70

---

# 5. Pflichtfelder

Jeder CrowEDU Node liefert mindestens:

temperature_celsius
humidity_percent

node_name

fw_version

esp_uptime_seconds

wifi_rssi

last_reboot

timestamp

---

# 6. Feldbeschreibung

temperature_celsius

Aktuelle Temperatur.

---

humidity_percent

Aktuelle Luftfeuchtigkeit.

---

node_name

Eindeutiger Name des Knotens.

---

fw_version

Installierte Firmware-Version.

---

esp_uptime_seconds

Laufzeit des Systems seit dem letzten Neustart.

---

wifi_rssi

WLAN-Signalstärke.

---

last_reboot

Zeitpunkt des letzten Neustarts.

---

timestamp

Zeitpunkt der Datenerfassung.

---

# 7. Beispiel

temperature_celsius 17.36
humidity_percent 57.70

node_name crowedu-node1

fw_version 20261104

esp_uptime_seconds 3899

wifi_rssi -46

last_reboot "2026-11-04 14:36:45"

timestamp "2026-11-04 15:31:39"

---

# 8. Änderungsregel

Neue Felder werden nicht direkt in dieses Dokument
aufgenommen.

Änderungswünsche werden zunächst im Backlog erfasst.

Eine Erweiterung erfolgt erst über
Node API Freeze V2.