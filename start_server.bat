@echo off
title The Oxford College of Engineering - Student Profile Management System
echo ========================================================================
echo    [+] THE OXFORD COLLEGE OF ENGINEERING - STUDENT PROFILE MANAGEMENT
echo ========================================================================
echo [*] Starting Python FastAPI and SQLite Database Server...
echo [*] Opening browser to http://localhost:8008 ...
start http://localhost:8008
python run_student.py
pause
