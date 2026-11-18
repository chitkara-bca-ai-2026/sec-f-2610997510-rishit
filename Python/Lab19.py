"""Lab 19 - Student Notes Management System (file handling)"""

import os

NOTES_FILE = "notes.txt"

MENU = """
Select an operation:
1. Write / Save Notes
2. View Saved Notes
3. Exit
"""


def write_notes():
    text = input("Enter notes to save: ").strip()
    if not text:
        print("[ERROR] Notes cannot be empty.")
        return
    try:
        # FIX: append mode ("a") so earlier notes are kept.
        # The original log used overwrite mode, so the second note erased the first.
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"[SUCCESS] Notes successfully saved to '{NOTES_FILE}'.")
    except OSError as err:
        print(f"[ERROR] Could not write to file: {err}")


def view_notes():
    print(f"\n--- Notes Content ({NOTES_FILE}) ---")
    if not os.path.exists(NOTES_FILE):
        print("No notes file exists yet. Please write some notes first.")
        return
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except OSError as err:
        print(f"[ERROR] Could not read file: {err}")
        return
    print(content if content else "The notes file is empty.")


def main():
    print("=" * 50)
    print("     STUDENT NOTES MANAGEMENT SYSTEM")
    print("=" * 50)
    while True:
        print(MENU)
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            write_notes()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("\nThank you for using the Notes Management System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-3.")


if __name__ == "__main__":
    main()
