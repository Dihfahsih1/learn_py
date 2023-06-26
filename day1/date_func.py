def date():
    import datetime
    to =datetime.datetime.today().date() 
    format_date = to.strftime("%d %B, %Y")
    format_time = to.strftime("%I:%M %p")
    weekday = to.strftime("%a")

    return format_date,format_time, weekday
