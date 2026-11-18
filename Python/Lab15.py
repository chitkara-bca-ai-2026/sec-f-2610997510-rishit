"""Lab 15 - Student Information Management System"""

students = {
    101: {"name": "Aman", "branch": "BCA AI", "sem": 1, "marks": [85, 90, 78]},
    102: {"name": "Riya", "branch": "BCA AI", "sem": 1, "marks": [92, 88, 95]},
    103: {"name": "Karan", "branch": "BCA AI", "sem": 1, "marks": [74, 80, 82]},
}

MENU = """
Select an operation:
1. View All Students
2. Search Student by Roll Number
3. Register New Student
4. Update Student Details
5. View Academic Performance
6. Delete Student Record
7. Exit
"""


def read_int(prompt, low=None, high=None, range_msg=None):
    """Keep asking until a valid integer (optionally within a range) is entered."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("  [ERROR] Please enter a valid integer.")
            continue
        if low is not None and high is not None and not (low <= value <= high):
            print(f"  [ERROR] {range_msg or f'Value must be between {low} and {high}.'}")
            continue
        return value


def read_marks():
    marks = []
    for i in range(1, 4):
        marks.append(read_int(f"  Subject {i}: ", 0, 100, "Marks must be between 0 and 100."))
    return marks


def print_row(roll, s):
    print(f"Roll No: {roll:<4} | Name: {s['name']:<10}| Branch: {s['branch']} "
          f"| Sem: {s['sem']} | Marks: {s['marks']}")


def view_all():
    print("\n--- Enrolled Student Records ---")
    if not students:
        print("No student records available.")
    for roll in sorted(students):
        print_row(roll, students[roll])
    print(f"Total Enrolled Students: {len(students)}")


def search_student():
    roll = read_int("Enter Roll Number to search: ")
    s = students.get(roll)
    if s is None:
        print(f"\n[ERROR] No student found with Roll No {roll}.")
        return
    print(f"\n[FOUND] Record for Roll No {roll}:")
    print(f"  Name     : {s['name']}")
    print(f"  Branch   : {s['branch']}")
    print(f"  Semester : {s['sem']}")
    print(f"  Marks    : {s['marks']}")


def register_student():
    print("\n--- Register New Student ---")
    roll = read_int("Enter Roll Number: ")
    if roll in students:
        print(f"[ERROR] Roll Number {roll} already exists.")
        return
    name = input("Enter Student Name: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty.")
        return
    branch = input("Enter Branch (e.g. BCA AI): ").strip() or "BCA AI"
    sem = read_int("Enter Semester: ", 1, 8, "Semester must be between 1 and 8.")
    print("Enter marks obtained in 3 subjects:")
    marks = read_marks()
    students[roll] = {"name": name, "branch": branch, "sem": sem, "marks": marks}
    print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")


def update_student():
    print("\n--- Update Student Details ---")
    roll = read_int("Enter Roll Number to update: ")
    s = students.get(roll)
    if s is None:
        print(f"[ERROR] No student found with Roll No {roll}.")
        return
    print("Which field do you want to update?")
    print("1. Name\n2. Branch\n3. Semester\n4. Marks")
    choice = read_int("Enter choice (1-4): ", 1, 4, "Please choose between 1 and 4.")
    if choice == 1:
        new_name = input("Enter new name: ").strip()
        if not new_name:
            print("[ERROR] Name cannot be empty.")
            return
        s["name"] = new_name
    elif choice == 2:
        new_branch = input("Enter new branch: ").strip()
        if not new_branch:
            print("[ERROR] Branch cannot be empty.")
            return
        s["branch"] = new_branch
    elif choice == 3:
        s["sem"] = read_int("Enter new semester: ", 1, 8, "Semester must be between 1 and 8.")
    else:
        print("Enter new marks for 3 subjects:")
        s["marks"] = read_marks()
    print(f"[SUCCESS] Record for Roll No {roll} updated.")


def view_performance():
    print("\n--- Academic Performance ---")
    roll = read_int("Enter Roll Number: ")
    s = students.get(roll)
    if s is None:
        print(f"[ERROR] No student found with Roll No {roll}.")
        return
    total = sum(s["marks"])
    maximum = 100 * len(s["marks"])
    percentage = total / maximum * 100
    result = "PASS" if percentage >= 40 and min(s["marks"]) >= 33 else "FAIL"
    print(f"Name        : {s['name']}")
    print(f"Marks       : {s['marks']}")
    print(f"Total Marks : {total} / {maximum}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Result      : {result}")


def delete_student():
    print("\n--- Delete Student Record ---")
    roll = read_int("Enter Roll Number to delete: ")
    s = students.pop(roll, None)
    if s is None:
        print(f"[ERROR] No student found with Roll No {roll}.")
        return
    print(f"[SUCCESS] Record of '{s['name']}' (Roll No: {roll}) deleted.")


def main():
    print("=" * 50)
    print("     STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 50)
    actions = {
        1: view_all,
        2: search_student,
        3: register_student,
        4: update_student,
        5: view_performance,
        6: delete_student,
    }
    while True:
        print(MENU)
        choice = read_int("Enter your choice (1-7): ", 1, 7, "Please choose between 1 and 7.")
        if choice == 7:
            print("\nThank you for using the Student Information Management System. Goodbye!")
            break
        actions[choice]()


if __name__ == "__main__":
    main()
