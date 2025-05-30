# 🛡️ Linux-Centric Cyber Threat Intelligence Framework

A proactive cyber threat detection framework designed for Linux (but tested on Windows), supporting real-time process scanning and IOC correlation using threat feeds from OTX or MISP. Includes a Flask-based web UI to monitor all running processes and detected threats.

---

## 🔍 Features

- Process name-based threat detection
- IOC ingestion from AlienVault OTX (with API key support)
- Web interface showing all running processes and detected threats
- Auto-refresh functionality
- Modular and Docker-ready design
- Public deployment supported (Render, etc.)

---

## 📁 Project Structure

```
linux_cti_framework/
│
├── core/
│   ├── threat_scanner.py        # Scans processes against IOCs
│   ├── event_correlator.py      # Matches processes with threat intelligence
│   └── process_list.py          # Lists all running processes
│
├── feeds/
│   └── otx_ingestor.py          # Pulls IOCs from AlienVault OTX
│
├── ui/
│   ├── app.py                   # Flask server & routing
│   └── templates/
│       └── index.html           # Web UI template
│
├── malware_sim.py              # Simulated malware (for safe testing)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- pip
- Virtual environment (optional)
- VS Code (optional but recommended)

---

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/linux-cti-framework.git
cd linux-cti-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Setup OTX API Key

Get your API key from https://otx.alienvault.com.

Set it in your terminal session or VS Code launch config:

```bash
# Temporarily
export OTX_API_KEY=your_key_here

# Or in Windows CMD
set OTX_API_KEY=your_key_here
```

---

## 🧪 Simulate Malware for Testing

Launch the simulation:

```bash
python malware_sim.py
```

This creates a real process named `python.exe` that sleeps for 10 minutes and mimics malware for testing purposes.

---

## 🖥️ Run the Web Interface

```bash
python ui/app.py
```

Visit: http://localhost:5000

You’ll see:
- ✅ Detected threats
- 🧩 All running processes

---

## 🐳 Docker Support

To build and run using Docker:

```bash
docker build -t linux-cti-framework .
docker run -p 5000:5000 -e OTX_API_KEY=your_key linux-cti-framework
```

---

## ☁️ Deployment

To host publicly:
- Use Render or Railway
- Set `OTX_API_KEY` as an environment variable in their UI
- Deploy `ui/app.py` as the entrypoint

---

## 📌 Notes

- This framework currently supports IOC detection via process names and simulated command-line patterns.
- Integration with file hash and domain/IP correlation is planned for future releases.

---
