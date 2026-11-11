# Installation

## Voraussetzungen

Für die Entwicklung werden benötigt:

- Python 3.13 oder neuer
- MariaDB
- Git
- Internetverbindung für Python-Pakete

### Debian 13 (Trixie)

```bash
sudo apt update

sudo apt install git python3.13-venv libmariadb-dev
```

---

## Schnellstart (Linux)

Hinweis:

Die eigentliche Anwendung befindet sich im Verzeichnis:

```text
backend/
```

Installation:

```bash
git clone https://github.com/haukefuchs-prog/CrowEDU-Backend.git

cd CrowEDU-Backend/backend

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Virtuelle Umgebung

### Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Nach Änderungen an der Datei `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Datenbank erstellen

MariaDB starten und anschließend:

```sql
CREATE DATABASE crowedu;
```

Die Tabellen werden gemäß der Dokumentation angelegt:

```text
docs/data-model-freeze-v1.md
```

---

## Konfiguration

Datei:

```text
config/config.py
```

Beispiel:

```python
DB_HOST = "localhost"
DB_PORT = 3306

DB_NAME = "crowedu"

DB_USER = "crowedu"
DB_PASSWORD = "password"
```

---

## Backend starten

### Entwicklungsbetrieb

```bash
python app.py
```

oder:

```bash
flask run
```

---

## Deployment mit systemd

Konfiguration:

```text
/etc/systemd/system/crowedu-backend.service
```

Dienst neu laden:

```bash
sudo systemctl daemon-reload
```

Dienst starten:

```bash
sudo systemctl start crowedu-backend
```

Autostart aktivieren:

```bash
sudo systemctl enable crowedu-backend
```

Status prüfen:

```bash
sudo systemctl status crowedu-backend
```

Logs anzeigen:

```bash
sudo journalctl -u crowedu-backend -f
```

---

## Funktionstest

Aufruf:

```text
http://127.0.0.1:5000/api/v1/health
```

oder:

```text
https://api.crowedu.de/api/v1/health
```

Erwartete Antwort:

```json
{
    "service": "CrowEDU Backend",
    "status": "ok",
    "version": "1.0"
}
```

---

# Entwicklungsumgebung

Empfohlene Werkzeuge:

- Visual Studio Code
- GitHub Desktop oder Git
- MariaDB
- Postman
- Bruno

---

# Entwicklungsablauf

1. Repository klonen
2. Virtuelle Umgebung erstellen
3. Abhängigkeiten installieren
4. Dokumentation lesen
5. Architektur-Freeze beachten
6. API-Freeze beachten
7. Implementierung beginnen

---

# Wichtige Dokumente

Vor der Entwicklung lesen:

```text
docs/architecture.md
docs/folder-structure-freeze-v1.md
docs/api-freeze-v1.md
docs/data-model-freeze-v1.md
docs/roadmap.md
```

Diese Dokumente bilden die verbindliche Grundlage für CrowEDU V1.