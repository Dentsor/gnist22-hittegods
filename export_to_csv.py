from datetime import datetime
import sqlite3
import csv
from typing import List, Text

def generate_csv_filename(table: Text) -> Text:
    return datetime.now().strftime(f"backups/%Y-%m-%d_%H.%M.%S-{table}.csv")

def export_to_csv(table: Text, filename: Text):
    with sqlite3.connect("src/db.sqlite3") as connection:
        c: sqlite3.Cursor = connection.cursor()
        c.execute(f"SELECT * FROM {table};")

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

def export_table(table: Text):
    filename: Text = generate_csv_filename(table)
    print(f"Exporting table '{table}' to '{filename}'...")
    export_to_csv(table, filename)
    print("Finished table export.")


def run_single_export():
    tables: List[Text] = [
        "hittegods_hittegods",
        "hittegods_oppdatering",
        "hittegods_kategori",
        "hittegods_type",
    ]
    print("\nExporting database to CSV...")
    for table in tables:
        export_table(table)
    print("Finished database export.\n")
