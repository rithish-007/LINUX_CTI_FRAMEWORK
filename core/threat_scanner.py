import psutil


def scan_processes(threat_iocs):
    detected = []
    print("[DEBUG] Threat IOCs:", threat_iocs)

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print("[DEBUG] Checking process:", proc.info['name'])
            if proc.info['name'] in threat_iocs.get('process_names', []):
                detected.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print("[DEBUG] Detected:", detected)
    return detected
