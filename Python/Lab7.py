print("=" * 40)
print("     CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

# 1. Take input from the user
year = int(input("Enter year: "))

# 2. Validate the input
if year <= 0:
    print("Error: Please enter a positive year.")
    exit()

# 3. Check whether the year is a leap year
if year % 400 == 0:
    leap_year = True
    reason = "Century year divisible by 400"
elif year % 100 == 0:
    leap_year = False
    reason = "Century year not divisible by 400"
elif year % 4 == 0:
    leap_year = True
    reason = "Divisible by 4 and not a century year"
else:
    leap_year = False
    reason = "Not divisible by 4"

# 4. Determine calendar details
if leap_year:
    february_days = 29
    total_days = 366
    status = "LEAP YEAR"
else:
    february_days = 28
    total_days = 365
    status = "COMMON YEAR"

# 5. Display the results
print("\n" + "-" * 40)
print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {total_days} days")
print(f"Days in February: {february_days} days")
print(f"Reason: {reason}")
print("-" * 40)