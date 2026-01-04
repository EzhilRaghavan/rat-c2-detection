from parsers.tcp_parser import get_tcp_flows
import statistics

def detect_beaconing(packets):
    flows = get_tcp_flows(packets)

    for flow, times in flows.items():
        if len(times) >= 5:
            intervals = [times[i+1] - times[i] for i in range(len(times)-1)]
            if statistics.pstdev(intervals) < 1:
                return True

    return False
