# date_calculation.py

import datetime
from leap_year import is_leap_year

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
        next_year += 1
    return next_year

def calculate_days_since_birth(birth_date):
    current_date = datetime.date.today()
    days = (current_date - birth_date).days
    leap_years_count = sum(1 for year in range(birth_date.year, current_date.year + 1) if is_leap_year(year))
    days_with_leap_years = days + leap_years_count
    return days_with_leap_years
