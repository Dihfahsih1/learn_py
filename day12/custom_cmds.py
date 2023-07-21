command =""
started =False
while True:
    command=input("> ").lower()
    if command =="start":
        if started:
            print("Car already started")
        else:
            started =True
            print("Car started...")

    elif command =="stop":
        if not started:
            print("car already stopped")
        else:
            started =False
            print("Car stopped....")

    elif command =="help":
        print("""
    start - to start car
    stop - to stop car
    quit - to  quit """)
    elif command =="quit":
        break

    else:
        print("the command you typed is invalid")
