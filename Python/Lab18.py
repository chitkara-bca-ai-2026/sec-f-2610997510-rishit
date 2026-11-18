"""Lab 18 - Mathematics Learning Tool (recursion: factorial & Fibonacci)"""

MAX_FIB_TERMS = 35  # plain recursive Fibonacci becomes very slow beyond this

MENU = """
Select an operation:
1. Calculate Factorial
2. Generate Fibonacci Series
3. Exit
"""


def factorial(n):
    """Recursive factorial."""
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Recursive n-th Fibonacci number (0-indexed: F0=0, F1=1)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def read_non_negative_int(prompt):
    """Return a non-negative int, or None after printing an error."""
    try:
        value = int(input(prompt).strip())
    except ValueError:
        print("[ERROR] Please enter a non-negative whole number.")
        return None
    if value < 0:
        print("[ERROR] Please enter a non-negative whole number.")
        return None
    return value


def factorial_option():
    n = read_non_negative_int("Enter a non-negative integer: ")
    if n is None:
        return
    # Python's default recursion limit is ~1000; stay safely under it.
    if n > 900:
        print("[ERROR] Number too large for recursion. Enter a value up to 900.")
        return
    print(f"[RESULT] Factorial of {n} ({n}!) = {factorial(n)}")


def fibonacci_option():
    n = read_non_negative_int("Enter number of terms to generate: ")
    if n is None:
        return
    if n > MAX_FIB_TERMS:
        print(f"[ERROR] Too many terms for plain recursion. Enter a value up to {MAX_FIB_TERMS}.")
        return
    series = [fibonacci(i) for i in range(n)]
    print(f"[RESULT] Fibonacci series ({n} terms): {series}")


def main():
    print("=" * 50)
    print("          MATHEMATICS LEARNING TOOL")
    print("=" * 50)
    while True:
        print(MENU)
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            factorial_option()
        elif choice == "2":
            fibonacci_option()
        elif choice == "3":
            print("\nThank you for using the Mathematics Learning Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1-3.")


if __name__ == "__main__":
    main()
