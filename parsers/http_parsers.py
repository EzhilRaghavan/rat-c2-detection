def get_http_payloads(packets):
    payloads = []

    for pkt in packets:
        if pkt.haslayer("Raw"):
            data = pkt["Raw"].load.decode(errors="ignore")
            payloads.append(data)

    return payloads
