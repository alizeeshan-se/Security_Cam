import csv
import os

def log_intruder(name, timestamp, image_path):
    log_file = "logs/log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name", "Timestamp", "ImagePath"])
        writer.writerow([name, timestamp, image_path])

    print("[LOG] Intruder details saved to log.")
