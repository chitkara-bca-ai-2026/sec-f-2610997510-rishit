"""Lab 16 - Enterprise Modular Utility Calculator"""

history = []

MENU = """
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus / Remainder (%)
6. Power / Exponentiation (Default: Square)
7. View Calculation History
8. Exit
"""


def fmt(n):
    """Show whole numbers without a trailing .0 (10.0 -> 10)."""
    return str(int(n)) if float(n).is_integer() else str(round(n, 10))


def read_number(prompt, allow_blank=False):
    while True:
        raw = input(prompt).strip()
        if allow_blank and raw == "":
            return None
        try:
            return float(raw)
        except ValueError:
            print("[ERROR] Please enter a valid number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return a % b


def power(base, exponent=2):
    return base ** exponent


def record(a, symbol, b, result):
    line = f"{fmt(a)} {symbol} {fmt(b)} = {fmt(result)}"
    history.append(line)
    print(f"[RESULT] {line}")


def binary_operation(func, symbol):
    a = read_number("Enter first number: ")
    b = read_number("Enter second number: ")
    try:
        record(a, symbol, b, func(a, b))
    except ZeroDivisionError as err:
        print(f"[ERROR] {err}")


def power_operation():
    base = read_number("Enter base number: ")
    exp = read_number("Enter exponent (press Enter for default square): ", allow_blank=True)
    if exp is None:
        exp = 2
    try:
        result = power(base, exp)
    except (OverflowError, ZeroDivisionError):
        print("[ERROR] Result is too large or undefined.")
        return
    if isinstance(result, complex):
        print("[ERROR] Result is not a real number.")
        return
    record(base, "^", exp, result)


def show_history():
    print("\n--- Calculation History ---")
    if not history:
        print("No calculations yet.")
    for i, line in enumerate(history, 1):
        print(f"{i}. {line}")


def main():
    print("=" * 50)
    print("     ENTERPRISE MODULAR UTILITY CALCULATOR")
    print("=" * 50)
    while True:
        print(MENU)
        choice = input("Enter your choice (1-8): ").strip()
        if choice == "1":
            binary_operation(add, "+")
        elif choice == "2":
            binary_operation(subtract, "-")
        elif choice == "3":
            binary_operation(multiply, "*")
        elif choice == "4":
            binary_operation(divide, "/")
        elif choice == "5":
            binary_operation(modulus, "%")
        elif choice == "6":
            power_operation()
        elif choice == "7":
            show_history()
        elif choice == "8":
            print("\nThank you for using the Utility Calculator. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
