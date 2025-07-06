@echo off
echo Installing dependencies from requirements.txt...
pip install --disable-pip-version-check --no-color --progress-bar on -r requirements.txt > nul 2>&1 || (
    echo ERROR occurred during installation:
    pip install --disable-pip-version-check --no-color -r requirements.txt
    exit /b 1
)
echo Installation completed successfully
pause