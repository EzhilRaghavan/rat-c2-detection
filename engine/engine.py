from capture.pcap_ingest import read_pcap
from capture.live_capture import capture_live
from detection.beaconing import detect_beaconing
from detection.dns_tunnel import detect_dns_tunnel
from detection.c2_logic import verdict

def run_engine(mode, source):
    if mode == "pcap":
        packets = read_pcap(source)
    elif mode == "live":
        packets = capture_live(source)
    else:
        print("[!] Invalid mode")
        return {}

    beacon = detect_beaconing(packets)
    dns = detect_dns_tunnel(packets)

    return {
        "Beaconing": beacon,
        "DNS Tunneling": dns,
        "Final Verdict": verdict(beacon, dns)
    }

