@echo off
SETLOCAL

REM Check for Python installation
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Check for pip installation
where pip >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

REM Install virtualenv if not already installed
pip show virtualenv >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo virtualenv is not installed. Installing virtualenv...
    pip install virtualenv
)

REM Create a virtual environment
echo Creating virtual environment...
virtualenv venv

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete. Virtual environment 'venv' is ready to use.
echo To activate the virtual environment, run: venv\Scripts\activate
ENDLOCAL