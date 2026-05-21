import os

from scanner import scan_directory
from database import save_baseline
from monitor import start_monitoring

WATCHED_DIR = "watched-files"

IGNORE_EXTENSIONS = [
    ".tmp",
    ".log",
    ".cache"
]


def initialize():

    print("[INFO] Creating initial baseline...")

    baseline = scan_directory(
        WATCHED_DIR,
        ignore_extensions=IGNORE_EXTENSIONS
    )

    save_baseline(baseline)

    print("[INFO] Baseline created successfully.")


if __name__ == "__main__":

    os.makedirs("watched-files", exist_ok=True)

    initialize()

    start_monitoring(WATCHED_DIR)