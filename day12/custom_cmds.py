command =""
started =False
while True:
    command=input("> ").lower()
    if command =="start":
        if started:
            print("Car already started")
        else:
            started =True
            print("Car started ...")

    elif command =="stop":
        if not started:
            print("car already stopped")
        else:
            started =False
            print("Car stopped ....")

    elif command =="help":
        print("=====================")
        print("""\n start - to start car \n stop - to stop car \n quit - to quit \n""")
        print("=====================")
        
    elif command =="quit":
        break

    else:
        print("the command you typed is invalid")
