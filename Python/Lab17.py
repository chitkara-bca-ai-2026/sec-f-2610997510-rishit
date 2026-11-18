"""Lab 17 - Student Records Management System"""

students = {
    101: {"name": "Aman", "marks": [85, 90, 78]},
    102: {"name": "Riya", "marks": [92, 88, 95]},
    103: {"name": "Karan", "marks": [74, 80, 82]},
}

MENU = """
Select an operation:
1. Display All Students
2. Add New Student
3. Search Student
4. Exit
"""


def read_int(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("  [ERROR] Please enter a valid integer.")
            continue
        if low is not None and high is not None and not (low <= value <= high):
            print(f"  [ERROR] Value must be between {low} and {high}.")
            continue
        return value


def format_record(roll, s):
    total = sum(s["marks"])
    average = total / len(s["marks"])
    return (f"Roll No: {roll:<4} | Name: {s['name']:<10}| Marks: {s['marks']} "
            f"| Total: {total} | Average: {average:.2f}%")


def display_all():
    print("\n--- All Student Records ---")
    for roll in sorted(students):
        print(format_record(roll, students[roll]))
    print(f"Total Students: {len(students)}")


def add_student():
    print("\n--- Add New Student ---")
    roll = read_int("Enter Roll Number: ")
    name = input("Enter Student Name: ").strip()
    print("Enter marks for 3 subjects:")
    marks = [read_int(f"  Subject {i}: ", 0, 100) for i in range(1, 4)]
    if roll in students:
        print(f"[ERROR] Roll Number '{roll}' already exists.")
        return
    if not name:
        print("[ERROR] Name cannot be empty.")
        return
    students[roll] = {"name": name, "marks": marks}
    print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")


def search_student():
    print()
    roll = read_int("Enter Roll Number to search: ")
    if roll in students:
        print("[RECORD FOUND]")
        print(format_record(roll, students[roll]))
    else:
        print(f"[ERROR] No student found with Roll Number '{roll}'.")


def main():
    print("=" * 50)
    print("     STUDENT RECORDS MANAGEMENT SYSTEM")
    print("=" * 50)
    while True:
        print(MENU)
        choice = input("Enter choice (1-4): ").strip()
        if choice == "1":
            display_all()
        elif choice == "2":
            add_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\nThank you for using the Student Records System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
