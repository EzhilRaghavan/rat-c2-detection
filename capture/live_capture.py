from scapy.all import sniff

def capture_live(interface, count=200):
    print(f"[*] Capturing live packets on {interface}")
    packets = sniff(iface=interface, count=count)
    return packets

