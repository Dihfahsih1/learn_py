def date():
    import datetime
    today =datetime.datetime.today().date() 
    format_date = today.strftime("%d %B, %Y")
    format_time = today.strftime("%I:%M %p")
    weekday = today.strftime("%a")

    return today, format_time, format_date, weekday
