import requests
import os

def get_otx_iocs():
    api_key = os.getenv("OTX_API_KEY")
    if not api_key:
        print("[ERROR] OTX_API_KEY environment variable not set.")
        return {"process_names": ["python"]}

    url = "https://otx.alienvault.com/api/v1/pulses/subscribed"
    headers = {"X-OTX-API-KEY": api_key}

    iocs = {"process_names": ["python"]}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for pulse in data.get("results", []):
                for indicator in pulse.get("indicators", []):
                    if indicator["type"] in ["hostname", "IPv4", "domain"]:
                        iocs["process_names"].append(indicator["indicator"])
        else:
            print(f"[ERROR] OTX API response code: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to fetch OTX data: {e}")

    return iocs
