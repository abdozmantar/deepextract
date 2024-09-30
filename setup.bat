@echo off
REM Change to the directory where your script is located
cd /d "%~dp0"

REM Create a virtual environment and install dependencies
python setup.py

pause
