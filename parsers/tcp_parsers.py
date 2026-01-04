def get_tcp_flows(packets):
    flows = {}

    for pkt in packets:
        if pkt.haslayer("IP") and pkt.haslayer("TCP"):
            key = (pkt["IP"].src, pkt["IP"].dst)
            flows.setdefault(key, []).append(pkt.time)

    return flows
