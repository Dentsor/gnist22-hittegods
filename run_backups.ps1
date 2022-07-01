# Create Python Virtual Environment
if (! (Test-Path -Path psenv)) {
    python3 -m venv psenv
}

# Activate Python Virtual Environment
./psenv/bin/Activate.ps1

# Install Python requirements
python3 -m pip install -r requirements.txt

python3 export_periodically.py
