def add(a, b):
    answer = a + b

    print(str(a) + " + " + str(b) + " = " + str(answer))


def sub(a, b):
    answer = a - b

    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a, b):
    answer = a * b

    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b

    print(str(a) + " / " + str(b) + " = " + str(answer))

#repeat the actions
while True:
        
    print("A, Addition")
    print("B, Subtraction")
    print("C, Multiplication")
    print("D, Division")
    print("E  Exit")

    choice = input("Input your Choice: ")
    FIRST_NUMBER = "Enter first number: "
    SECOND_NUMBER = "Enter second number: "
    if choice == "a" or choice == "A":
        print("Addition ")
        a=int(input(FIRST_NUMBER))
        b=int(input(SECOND_NUMBER))
        add(a,b)

    elif choice == "b" or choice == "B":
        print("Subtraction ")
        a=int(input(FIRST_NUMBER))
        b=int(input(SECOND_NUMBER))
        sub(a,b)

    elif choice == "c" or choice == "C":
        print("Multiplication ")
        a=int(input(FIRST_NUMBER))
        b=int(input(SECOND_NUMBER))
        mult(a,b)

    elif choice == "d" or choice == "D":
        print("Division ")
        a=int(input(FIRST_NUMBER))
        b=int(input(SECOND_NUMBER))
        div(a,b)

    elif choice == "e" or choice == "E":
        print("Program Ended ")
        quit()
    

