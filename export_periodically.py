from datetime import datetime, timedelta
import time
from typing import Text
import export_to_csv

# 60 seconds * 60 minutes * 8 hours
TIME_BETWEEN_EXPORTS = 60*60*8

while True:
    export_to_csv.run_single_export()

    nextRun: Text = (datetime.now() + timedelta(seconds=TIME_BETWEEN_EXPORTS)).strftime("%Y-%m-%d %H:%M:%S")
    print(f"Sleeping for {TIME_BETWEEN_EXPORTS} seconds. Next export at {nextRun}...")

    time.sleep(TIME_BETWEEN_EXPORTS)
