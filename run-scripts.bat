@echo off
setlocal

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install required packages
python .\scripts\test_ws.py

REM Deactivate the virtual environment
deactivate

echo Script complete
pause