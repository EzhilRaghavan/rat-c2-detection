def get_dns_queries(packets):
    queries = []

    for pkt in packets:
        if pkt.haslayer("DNS") and pkt["DNS"].qd:
            qname = pkt["DNS"].qd.qname.decode(errors="ignore")
            queries.append(qname)

    return queries
