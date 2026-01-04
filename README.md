# RAT C2 Traffic Analysis & Detection Engine

# Overview
Behavior-based network detection engine to identify Remote Access Trojan (RAT) Command-and-Control (C2) traffic  
Supports both offline PCAP analysis and live network traffic monitoring  
Focuses on communication behavior instead of malware signatures or payload inspection  

# Detection Capabilities

# Beaconing Detection
Identifies periodic and automated TCP communication patterns  
Detects low-variance timing intervals common in RAT C2 beacons  
Flags suspicious callback behavior used by remote controllers  

# DNS Tunneling Detection
Detects covert C2 communication and data exfiltration over DNS  
Identifies abnormally long DNS query names  
Uses entropy analysis to detect encoded or obfuscated payloads in DNS  

# C2 Correlation Logic
Correlates beaconing and DNS indicators for higher confidence detection  
Reduces false positives by combining multiple behavioral signals  
Produces a final verdict based on aggregated evidence  

# Techniques Used
TCP flow timing analysis  
Beacon interval deviation analysis  
DNS query length inspection  
Shannon entropy calculation  
Multi-indicator behavioral correlation  

# Project Structure
rat-c2-detection/  
├── main.py                     Entry point and execution controller  
├── engine/  
│   └── engine.py               Core detection orchestration engine  
├── capture/  
│   ├── pcap_ingest.py          PCAP file ingestion logic  
│   └── live_capture.py         Live network packet capture module  
├── parsers/  
│   ├── tcp_parser.py           TCP traffic parsing  
│   ├── dns_parser.py           DNS traffic parsing  
│   └── http_parser.py          HTTP traffic parsing  
├── detection/  
│   ├── beaconing.py            Beaconing detection logic  
│   ├── dns_tunnel.py           DNS tunneling detection logic  
│   └── c2_logic.py             Indicator correlation and verdict logic  
└── output/  
    └── alerts.json             Detection results and alerts  

# Execution Flow
Select input source between PCAP file and live interface  
Capture or ingest network packets  
Parse protocol-specific traffic  
Execute behavioral detection logic  
Correlate indicators and generate final verdict  

# Installation
Requires Python 3.x  
Uses Scapy for packet capture and packet analysis  

# Usage

# PCAP Analysis
python3 main.py pcap sample.pcap  

# Live Traffic Monitoring
sudo python3 main.py live eth0  

# Output
Displays detection verdict in console  
Generates structured alert output for analysis  
Enables SOC-style review of suspicious traffic  

# Design Principles
Behavior-based detection over signature matching  
Modular and readable architecture  
SOC-aligned detection workflow  
Extensible detection framework  

# What This Project Demonstrates
Practical detection engineering skills  
Network traffic behavior analysis expertise  
Understanding of real-world RAT C2 techniques  
Blue team and SOC-relevant implementation  

# Applicable Roles
SOC Analyst  
Detection Engineer  
Network Security Analyst  
Cybersecurity Researcher  
