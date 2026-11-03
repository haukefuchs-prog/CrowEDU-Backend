# Installation

## Voraussetzungen

Für die Entwicklung werden benötigt:

- Python 3.13 oder neuer
- MariaDB
- Git
- Internetverbindung für Python-Pakete

---

## Repository klonen

```bash
git clone https://github.com/haukefuchs-prog/CrowEDU-Backend.git
cd CrowEDU-Backend/backend
```

---

## Virtuelle Umgebung erstellen

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

---

## Abhängigkeiten installieren

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

Beispiel:

config/config.py

```python
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "crowedu"
DB_USER = "crowedu"
DB_PASSWORD = "password"
```

---

## Backend starten

```bash
python app.py
```

oder später

```bash
flask run
```

---

## Funktionstest

Aufruf im Browser:

```text
http://127.0.0.1:5000/api/v1/health
```

Erwartete Antwort:

```json
{
    "status": "ok"
}
```

---

# Entwicklungsumgebung

Empfohlene Werkzeuge:

- Visual Studio Code
- GitHub Desktop oder Git
- MariaDB
- Postman oder Bruno für API-Tests

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