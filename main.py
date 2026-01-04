import sys
from engine.engine import run_engine

def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("PCAP : python3 main.py pcap file.pcap")
        print("LIVE : sudo python3 main.py live eth0")
        return

    mode = sys.argv[1]
    source = sys.argv[2]

    print("[*] RAT C2 Detection Started")
    result = run_engine(mode, source)

    print("\n--- Detection Result ---")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

