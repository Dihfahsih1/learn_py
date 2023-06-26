from date_func import date 
def welcome():
    format_date=date.format_date
    format_time=date.format_time
    weekday=date.weekday
    name = input("What is your name?")
    #validating the user input
    while not name.isalpha():
        print(f"Please enter only characters, your name {name} contained numbers or symbols")
        name = input("What is your name?")
    print(f"Hey {name} you joined us at {format_time}\n, {format_date} \n on a {weekday}")

welcome()