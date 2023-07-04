from datetime import datetime, date

def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def count_leap_years(start_year, end_year):
    count = 0
    leap_years = []
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            count += 1
            leap_years.append(year)
    return count, leap_years

def next_leap_year(year):
    next_year = year + 1
    while not is_leap_year(next_year):
        next_year +=1
    return next_year

def calculate_days_since_birth(b_date):
    current_date = date.today()
    days = (current_date - b_date).days
    leap_years_count = sum(1 for year in range(b_date.year, current_date.year + 1) if is_leap_year(year))
    days_with_leap_years = days + leap_years_count
    return days_with_leap_years

# Prompt the user to enter their date of birth
dob = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    year, month, day = map(int, dob.split('-'))
    birth_date = date(year, month, day)
    days_since_birth = calculate_days_since_birth(birth_date)
    birth_year = year
    current_year = datetime.now().year
    nxt_year = next_leap_year(current_year)
    leap_years_count, leap_years_list = count_leap_years(birth_year, current_year)

    print("Number of days since your birth, including leap years:", days_since_birth, "days")
    print(f"The number of leap years between {birth_year} and {current_year} is: {leap_years_count}")
    print(f"The leap years between {birth_year} and {current_year} are: {leap_years_list}")
    print(f"The next leap year after {current_year} is {nxt_year}")

except ValueError:
    print("Invalid date of birth. Please enter a valid date in the format YYYY-MM-DD.")
