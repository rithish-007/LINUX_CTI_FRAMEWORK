import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, render_template
from core.threat_scanner import scan_processes
from core.event_correlator import correlate
from feeds.otx_ingestor import get_otx_iocs
import psutil  # <--- Import psutil to get process info

app = Flask(__name__)

@app.route('/')
def dashboard():
    threat_iocs = get_otx_iocs()
    raw_events = scan_processes(threat_iocs)
    correlated = correlate(raw_events, threat_iocs)

    # New code to get all running processes
    all_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            all_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Pass all_processes to the template along with detected threats
    return render_template("index.html", events=correlated, all_processes=all_processes)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
