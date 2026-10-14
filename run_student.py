"""
Student Profile Management System - Standalone Launcher
Starts the FastAPI Backend and Web Portal at http://localhost:8080
"""
import os
import sys
import webbrowser

# Force UTF-8 stdout on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import socket
import uvicorn

def find_available_port(preferred_ports=[8008, 8000, 5000, 8088]):
    for p in preferred_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', p))
                return p
        except OSError:
            continue
    return 8008

def main():
    port = find_available_port()
    print("=" * 72)
    print("   [+] STUDENT PROFILE MANAGEMENT SYSTEM (THE OXFORD COLLEGE OF ENGINEERING)")
    print("=" * 72)
    print("[*] Initializing TOCE SQLite Database (students.db)...")
    print(f"[*] Launching Oxford Academic Portal at: http://localhost:{port}")
    print("[*] Frontend HTML file available at: frontend/student.html")
    print("[*] Press Ctrl+C to shutdown the server.")
    print("=" * 72)

    # Set working directory to project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    sys.path.insert(0, project_root)

    # Open browser automatically after a short delay
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass

    uvicorn.run("backend.student_api:app", host="127.0.0.1", port=port, reload=False, log_level="info")

if __name__ == "__main__":
    main()
