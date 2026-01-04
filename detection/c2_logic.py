def verdict(beaconing, dns):
    if beaconing and dns:
        return "CONFIRMED RAT C2"
    elif beaconing or dns:
        return "SUSPICIOUS TRAFFIC"
    else:
        return "NO C2 ACTIVITY"
