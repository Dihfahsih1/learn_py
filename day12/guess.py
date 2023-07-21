guess = 9
guess_count =0
guess_limit = 5
while guess_count < guess_limit:
    guess_input =int(input("Enter your guess: "))
    guess_count  +=1
    if guess_input == guess:
        print("Your guess is correct")
        break
    else:
        print("your guess was not correct")
