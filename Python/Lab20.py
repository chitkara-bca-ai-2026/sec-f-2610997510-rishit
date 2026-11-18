"""Lab 20 - Office Daily Log Book (file handling, append mode)"""

import os
from datetime import datetime

LOG_FILE = "daily_log.txt"

DEFAULT_ENTRIES = [
    "09:00 AM - System server startup verified.",
    "10:30 AM - Morning attendance synchronized.",
    "02:15 PM - Network security patch applied.",
]

MENU = """
Select an operation:
1. Add Log Entry
2. Display Complete Log
3. Exit
"""


def ensure_log_file():
    """Create the log file with the starting entries if it doesn't exist yet."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(DEFAULT_ENTRIES) + "\n")


def add_entry():
    text = input("Enter log entry: ").strip()
    if not text:
        print("[ERROR] Log entry cannot be empty.")
        return
    timestamp = datetime.now().strftime("%I:%M %p")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{timestamp} - {text}\n")
        print(f"[SUCCESS] New entry logged to '{LOG_FILE}'.")
    except OSError as err:
        print(f"[ERROR] Could not write to log file: {err}")


def display_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            entries = [line.strip() for line in f if line.strip()]
    except OSError as err:
        print(f"[ERROR] Could not read log file: {err}")
        return
    print("\n=============== DAILY LOG BOOK ===============")
    for i, entry in enumerate(entries, 1):
        print(f"[{i:02d}] {entry}")
    print(f"\nTotal Logged Entries: {len(entries)}")
    print("==============================================")


def main():
    ensure_log_file()
    print("=" * 50)
    print("            OFFICE DAILY LOG BOOK")
    print("=" * 50)
    while True:
        print(MENU)
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
            display_log()
        elif choice == "3":
            print("\nThank you for using the Daily Log Book. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-3.")


if __name__ == "__main__":
    main()
