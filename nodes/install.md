# CrowEDU Node V1 – Installations-Checkliste

## 1. Repository klonen

```bash
cd ~

git clone https://github.com/haukefuchs-prog/CrowEDU-Backend.git
```

---

## 2. In das Raspberry-Verzeichnis wechseln

```bash
cd CrowEDU-Backend/backend-raspi
```

Prüfen:

```bash
ls -la
```

Vorhanden sein sollten mindestens:

```text
api.py
requirements.txt
sensors/
leds/
```

---

## 3. Virtuelle Python-Umgebung anlegen

```bash
python3 -m venv venv
```

---

## 4. Virtuelle Umgebung aktivieren

```bash
source venv/bin/activate
```

Der Prompt sollte nun beginnen mit:

```text
(venv)
```

---

## 5. Prüfen, ob das venv aktiv ist

```bash
which python
which pip
```

Erwartete Ausgabe:

```text
.../backend-raspi/venv/bin/python
.../backend-raspi/venv/bin/pip
```

Wenn dort `/usr/bin/...` steht, ist das venv nicht aktiv.

---

## 6. Python-Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

Warten bis alle Pakete erfolgreich installiert wurden.

---

## 7. API starten

```bash
python api.py
```

Erwartete Ausgabe:

```text
* Serving Flask app 'api'
* Running on ...
```

---

## 8. API testen

Im Browser:

```text
http://<RASPI-IP>:5000/metrics
```

oder lokal:

```bash
curl localhost:5000/metrics
```

Beispiel:

```text
temperature_celsius 15.83
humidity_percent 53.19
node_name "crowedu-node1"
fw_version "1.0.0"
node_uptime_seconds 12
wifi_rssi -999
last_reboot "..."
timestamp "..."
```

---

# Häufige Fehler

## Fehler

```text
ModuleNotFoundError: No module named 'flask'
```

### Ursache

Pakete wurden noch nicht installiert.

### Lösung

```bash
source venv/bin/activate
pip install -r requirements.txt
```

---

## Fehler

```text
externally-managed-environment
```

### Ursache

`pip` wurde außerhalb des venv ausgeführt.

### Lösung

```bash
source venv/bin/activate
```

danach erneut:

```bash
pip install -r requirements.txt
```

---

## Fehler

```text
Address already in use
Port 5000 is in use
```

### Ursache

Die API läuft bereits als systemd-Service.

### Lösung

```bash
sudo systemctl stop crowedu-api.service
```

oder einen anderen Port verwenden.

---

# Erfolgreicher Test

✅ GitHub Repository erfolgreich geklont

✅ Virtuelle Python-Umgebung erstellt

✅ Abhängigkeiten installiert

✅ Flask gestartet

✅ Sensoren erkannt

✅ `/metrics` liefert Messwerte

✅ Installation auf Test-Raspberry erfolgreich durchgeführt

---

**Stand:** Node API Freeze V1  
**Getestet auf:** crowedu-node1  
**Status:** Erfolgreich reproduzierbar 🚀