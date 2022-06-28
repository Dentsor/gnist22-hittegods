from datetime import datetime
import sqlite3
import csv
from typing import Text

def generate_csv_filename() -> Text:
    return datetime.now().strftime("backups/%Y-%m-%d_%H.%M.%S.csv")

def backup_to_csv(filename: Text):
    with sqlite3.connect("src/db.sqlite3") as connection:
        c: sqlite3.Cursor = connection.cursor()
        c.execute("SELECT * FROM hittegods_hittegods;")

        columns = [column[0] for column in c.description]
        results = []
        for row in c.fetchall():
            results.append(dict(zip(columns, row)))
        with open(filename, "w", newline='') as file:
            fieldnames = columns
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for line in results:
                writer.writerow(line)

def run_single_export():
    filename: Text = generate_csv_filename()
    print(f"Exporting database to '{filename}'...")
    backup_to_csv(filename)
    print("Finished database export.")
