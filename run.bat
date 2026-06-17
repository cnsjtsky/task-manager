@echo off
set PYTHONDONTWRITEBYTECODE=1
echo ==================================================
echo   LAUNCHING YOUR TASK MANAGER APPLICATION...
echo ==================================================

:: 1. Check if the virtual environment exists. If not, create it automatically.
if not exist venv (
    echo [1/3] No virtual environment found. Creating one now...
    python -m venv venv
) else (
    echo [1/3] Virtual environment found!
)

:: 2. Activate the virtual environment using standard Windows Batch (bypasses PowerShell blocks)
echo [2/3] Activating environment...
call venv\Scripts\activate.bat

:: 3. Silently check/install requirements
echo [3/3] Checking dependencies (this may take a moment on first run)...
pip install -r requirements.txt --quiet

:: 4. Start the server
echo --------------------------------------------------
echo SUCCESS! Your local server is running.
echo Click or copy this link into your browser: http://127.0.0.1:8000
echo --------------------------------------------------
echo To stop the server, just close this window.
echo --------------------------------------------------

python -m uvicorn main:app --reload

pause