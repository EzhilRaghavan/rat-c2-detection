from parsers.dns_parser import get_dns_queries
import math

def entropy(data):
    probs = [data.count(c)/len(data) for c in set(data)]
    return -sum(p * math.log2(p) for p in probs)

def detect_dns_tunnel(packets):
    queries = get_dns_queries(packets)

    for q in queries:
        if len(q) > 30 and entropy(q) > 4:
            return True

    return False

