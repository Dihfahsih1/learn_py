import datetime
from date_calculation import calculate_days_since_birth, count_leap_years, next_leap_year

def get_birth_date_from_input():
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    year, month, day = map(int, dob.split('-'))
    return datetime.date(year, month, day)

def main():
    birth_date = get_birth_date_from_input()
    days_since_birth = calculate_days_since_birth(birth_date)
    birth_year = birth_date.year
    current_year = datetime.datetime.now().year
    leap_years_count, leap_years_list = count_leap_years(birth_year, current_year)
    nxt_year = next_leap_year(current_year)

    print("Number of days since your birth, including leap years: ", str(days_since_birth) + " days")
    print(f"The number of leap years between {birth_year} and {current_year} is: {leap_years_count}")
    print(f"The leap years between {birth_year} and {current_year} are: {leap_years_list}")
    print(f"The next leap year after {current_year} is {nxt_year}")

if __name__ == '__main__':
    main()
