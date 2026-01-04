from scapy.all import rdpcap

def read_pcap(file):
    packets = rdpcap(file)
    print(f"[*] Loaded {len(packets)} packets from PCAP")
    return packets
