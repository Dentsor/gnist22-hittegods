date=$(date +"%Y.%m.%d-%H.%M.%S")
mkdir -p backups
cp src/db.sqlite3 backups/$date.sqlite3
