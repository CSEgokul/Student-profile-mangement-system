"""
IoT-Sentinel: One-Command System Launcher
Starts the FastAPI Backend and Cyber SOC Frontend at http://localhost:8000
"""
import os
import sys

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import uvicorn

def main():
    print("=" * 70)
    print("   [+] IoT-SENTINEL: THREAT DETECTION & ACTIVE DEFENSE SYSTEM")
    print("=" * 70)
    print("[*] Initializing AI models & Synthetic IoT Network Topology...")
    print("[*] Launching Web SOC Dashboard at: http://localhost:8000")
    print("[*] Press Ctrl+C to shutdown.")
    print("=" * 70)

    # Change working directory to project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    sys.path.insert(0, project_root)

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False, log_level="info")

if __name__ == "__main__":
    main()
