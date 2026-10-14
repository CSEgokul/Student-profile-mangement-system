# 🛡️ IoT-Sentinel: IoT Network Security Threat Detection & Prevention System

> **An Enterprise-Grade, Real-Time AI/ML Intrusion Detection & Active Defense System (IDS/IPS) for Heterogeneous Internet of Things (IoT) Networks.**

---

## 📌 Executive Summary

**IoT-Sentinel** is a full-stack cybersecurity platform engineered to detect, classify, explain, and mitigate network intrusions across diverse IoT ecosystems (Smart Home, Industrial SCADA/ICS, IoMT Healthcare, Connected Surveillance, Smart Grid).

It integrates **hybrid detection engines** (Unsupervised Isolation Forest + Supervised Multi-Class Ensembles + Heuristic Signature Rules), an **Explainable AI (XAI)** attribution layer, an **Intrusion Prevention System (IPS)** with automated device isolation, and a modern **Cyber SOC Dashboard** featuring real-time interactive topology visualization, deep packet inspection (DPI), and a **Red Team Attack Injection Studio**.

---

## 🚀 Key Features

### 1. 🌐 Heterogeneous IoT Protocol & Network Simulator
- Emits realistic, continuous telemetry across multiple protocols:
  - **MQTT** (Smart HVAC, Smart Locks, Energy Meters)
  - **Modbus-TCP** (Industrial PLC & SCADA safety valves)
  - **CoAP** (Healthcare Patient ECG Monitors, Air Quality Sensors)
  - **RTSP / HTTP** (4K Surveillance Cameras)
- Full OSI dissection with Layer 2 (Ethernet), Layer 3 (IPv4/IPv6), Layer 4 (TCP/UDP), Layer 7 (Application Payload), and Wireshark-style **Hex Dump + ASCII Decoder**.

### 2. 🎯 Red Team Cyberattack Generator
Injects live simulated cyberattacks with customizable intensity, duration, and target devices:
- **Mirai Botnet SYN Flood & Telnet Brute Force** (Port 23 credential stuffing + volumetric DDoS)
- **MQTT Command Injection & Payload Poisoning** (Unauthorized topic wildcards & actuator manipulation)
- **Industrial SCADA / Modbus Coil Override** (Illegal Function Code 0x05 safety valve actuation)
- **ARP Cache Poisoning (Man-in-the-Middle)** (Gateway spoofing & MITM interception)
- **CoAP Reflection & UDP Amplification Flood** (14x amplification attack on UDP 5683)
- **Firmware RCE & C2 Reverse Shell Beaconing** (Remote command injection & heartbeat beaconing)
- **Zero-Day Statistical Anomaly Burst** (High-entropy novel packet distribution)
- **Reconnaissance Port Sweep** (Nmap-style multi-port vulnerability sweep)

### 3. 🧠 Hybrid AI/ML Intrusion Detection Engine
- **Unsupervised Anomaly Detection**: `IsolationForest` continuously profiles statistical baselines to compute dynamic anomaly scores (0.0 to 1.0) and flag novel 0-day threats.
- **Supervised Multi-Class Classifier**: `RandomForestClassifier` trained on 10 flow features (Packet Rate, Byte Rate, SYN/ACK ratios, Shannon Payload Entropy, Port Diversity, Inter-Arrival Jitter) achieving **>98% accuracy** on CIC-IoT-2023 / IoT-23 inspired benchmarks.
- **Signature & Heuristic Rule Matcher**: Sub-millisecond pattern matcher inspecting CVE signatures, Telnet default credentials, and illegal protocol command codes.

### 4. 🔍 Explainable AI (XAI) & MITRE ATT&CK Mapping
- Provides transparent **feature contribution percentages** (SHAP/LIME-style attribution) explaining *why* an alert fired.
- Maps every detected threat to standard **MITRE ATT&CK for IoT** techniques (e.g. *T1498 Direct Network Flood, T0855 Unauthorized Command Message, T1078 Valid Accounts, T1557 ARP Poisoning, T1046 Network Service Scanning*).

### 5. 🛡️ Active Intrusion Prevention System (IPS)
- **Dynamic Firewall Drop Rules**: Automatically inserts `DROP` rules for malicious IP addresses.
- **Device Micro-segmentation & Quarantine**: Quarantines compromised MAC addresses to protect the wider IoT subnet.
- **Dynamic Rate Throttling**: Applies traffic rate-limiting on suspicious reconnaissance sweeps.
- **Human-in-the-loop Controls**: Manual IP unblocking, quarantine release, and rule resets.

### 6. 📊 Offline Dataset & PCAP Batch Analyzer
- Drag-and-drop CSV log analyzer with full classification report, confusion matrix, and one-click exportable **Forensic Incident Report (JSON)**.

---

## 🏗️ System Architecture

```
                                  [ Red Team Attack Studio ]
                                               │
                                               ▼
[ Heterogeneous IoT Devices ] ───► [ Packet Sniffing & Feature Extractor ]
  (MQTT, CoAP, Modbus, RTSP)                   │
                                               ▼
                               ┌───────────────────────────────┐
                               │     Hybrid Detection Engine   │
                               ├───────────────────────────────┤
                               │ • Signature Rule Matcher      │
                               │ • Isolation Forest Anomaly    │
                               │ • Random Forest Multi-Class   │
                               │ • Explainable AI (XAI)        │
                               └───────────────┬───────────────┘
                                               │
                        ┌──────────────────────┴──────────────────────┐
                        ▼                                             ▼
         [ Active Defense / IPS Engine ]              [ WebSocket Telemetry Stream ]
          • Dynamic Firewall DROP Rules                               │
          • Device MAC Quarantine                                     ▼
          • Rate Throttling                             [ Cyber SOC Web Dashboard ]
                                                          • Interactive Topology Map
                                                          • Real-time Alert Feed
                                                          • Deep Packet Hex Viewer
                                                          • Model Confusion Matrix
```

---

## 📁 Directory Structure

```
iot-sentinel/
├── backend/
│   ├── main.py                  # FastAPI app with REST & WebSocket telemetry broadcaster
│   ├── network_simulator.py      # Virtual IoT topology & heterogeneous packet generator
│   ├── attack_engine.py          # Red team attack simulation engine (8 attack vectors)
│   ├── ml_detector.py            # Isolation Forest + Random Forest classifier + XAI
│   ├── signature_engine.py       # Heuristic & Snort-style rule-based detection
│   ├── ips_engine.py             # Active defense firewall & MAC quarantine controller
│   └── dataset_manager.py        # Benchmark dataset generator & batch CSV analyzer
├── frontend/
│   ├── index.html                # Modern Cyber SOC Web Application
│   ├── css/
│   │   └── style.css             # Cyberpunk dark mode & glassmorphism styling
│   └── js/
│       ├── app.js                # Core WebSocket coordinator & state store
│       ├── topology.js           # HTML5 Canvas interactive IoT network graph
│       ├── attack_controller.js  # Attack injection triggers & countdown timer
│       ├── packet_inspector.js   # Deep Packet Inspection (DPI) & Hex dump modal
│       ├── xai_visualizer.js     # Explainable AI feature attribution bars
│       └── charts.js             # Real-time traffic & anomaly line charts
├── sample_data/
│   └── cic_iot_sample_traffic.csv# Sample IoT network flow dataset
├── run.py                        # One-command system launcher
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚡ Quick Start Guide

### Prerequisites
- Python 3.10+ (Python 3.11, 3.12, 3.13, 3.14 fully supported)
- Modern web browser (Chrome, Edge, Firefox)

### Step 1: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 2: Launch the System
```powershell
python run.py
```

### Step 3: Open the SOC Dashboard
Navigate to:
```
http://localhost:8000
```

---

## 🎮 Interactive Demonstration Walkthrough

1. **Observe Ambient IoT Traffic**:
   - Watch normal telemetry packets (MQTT, CoAP, Modbus) flowing between IoT sensors, the Edge Gateway, and the Fog Server.
   - All nodes will glow green (Healthy).
2. **Launch a Mirai Botnet Attack**:
   - Switch to the **Red Team Studio** tab.
   - Select **Mirai Botnet SYN Flood**, select **IP Camera (192.168.1.102)** as the target, set intensity to **7**, and click **Launch Simulated Attack**.
   - Return to the **Live SOC** tab:
     - The IP Camera immediately glows **crimson** and flashes with warning rings.
     - The Alert Feed displays: `🚨 CRITICAL: Mirai Botnet Telnet Brute Force / SYN Flood (MITRE T1498.001)`.
     - The **Active IPS** tab shows the attacker IP `198.51.100.77` added to the firewall blacklist and the camera isolated.
3. **Inspect Explainable AI (XAI)**:
   - Click on the **Explainable AI (XAI)** tab to observe real-time feature attribution (e.g. `Packet Rate: +45%`, `SYN Ratio: +38%`, `Port Sensitivity: +12%`).
4. **Deep Packet Inspection (DPI)**:
   - In the Live SOC tab, click on any packet in the table to open the **Hex Dump Modal** showing raw packet bytes and OSI layers.
5. **Evaluate Benchmark Dataset**:
   - Go to **Dataset & Forensics** and click **Evaluate Benchmark Dataset (CIC-IoT-2023)** to benchmark 600 flows with instant classification metrics.
6. **Export Forensic Security Report**:
   - Click **Forensic Report** in the top navigation bar to download an audit-ready JSON report.

---

## 👨‍💻 Technologies Used
- **Backend**: Python 3.14, FastAPI, WebSockets, Scikit-Learn, NumPy, Pandas, Uvicorn
- **Frontend**: HTML5 Canvas, Vanilla Modern JavaScript (ES6+), Vanilla CSS3 Design System, Chart.js, FontAwesome
- **Standards & Frameworks**: MITRE ATT&CK for IoT, CIC-IoT-2023 Flow Feature Model, Snort/Suricata Rule Heuristics
