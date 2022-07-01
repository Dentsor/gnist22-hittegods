# Gnist 2022 - Hittegods

**NB:** To back up/export the database periodically, see [Backups](#backups)

## Set up

Choose the set up instructions for your system:

### Windows

Run the Powershell-script:
```powershell
./run_with_powershell.ps1
```

If you wish to export/back up the database periodically, run the other Powershell-script:
```powershell
./run_backups.ps1
```

### Mac / Linux

You may install Powershell and use the script above, or use the `makefile` as follows:

```bash
# To "kick-start" the process, run 'make all' to run everything necessary and start the server
make all
```
or
```bash
# If necessary, remove database (removes all data! Be careful!)
#rm src/db.sqlite3

# Install dependencies
make install

# Run migrations
make migrate

# Create user
make createsuperuser

# Collect static files
make staticfiles

# Load initial data (optional)
make loaddata

# Start server
make start
```

## Backups

The Python-script `./export_periodically.py` will run an export of the database to CSV every 8 hours from start-time.

If you have Powershell installed, you may use the Powershell-script to launch Python with all dependencies:

```powershell
./run_backups.ps1
```
