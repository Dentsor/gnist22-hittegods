# Create Python Virtual Environment
if (! (Test-Path -Path psenv)) {
    python3 -m venv psenv
}

# Activate Python Virtual Environment
./psenv/bin/Activate.ps1

# Install Python requirements
python3 -m pip install -r requirements.txt

# Run migrations
python3 src/manage.py migrate

# Extract static files
python3 src/manage.py collectstatic

# Load initial data
python3 src/manage.py loaddata "src/hittegods/seeds/data_dump.json"

# Create user
do {
    $CreateUser = Read-Host "Vil du opprette en ny bruker? (Må gjøres ved førstegangsoppsett) (Ja/Nei): "
} while (!(@("Ja", "Y", "Nei", "N") -contains $CreateUser))

if (@("Ja", "Y") -contains $CreateUser) {
    python3 src/manage.py createsuperuser
}

python3 src/manage.py runserver localhost:8000
