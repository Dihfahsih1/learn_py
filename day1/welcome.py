import date_func
def welcome():
    format_time, format_date, weekday = date_func.date()
    name = input("What is your name?")
    #validating the user input
    while not name.isalpha():
        print(f"Please enter only characters, your name {name} contained numbers or symbols")
        name = input("What is your name?")
    print(f"Hey {name} you joined us at {format_time}\n, {format_date} \n on a {weekday}")

welcome()