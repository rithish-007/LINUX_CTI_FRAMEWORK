def correlate(processes, iocs):
    matches = []
    indicators = set(iocs.get("process_names", []))
    for proc in processes:
        if proc["name"] in indicators:
            matches.append(proc)
    return matches
