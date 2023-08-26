# Guess the Word Mini-Project

import random

# List of words for the game
word_list = ["python", "programming", "computer", "code", "developer", "learning"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to 'Guess the Word' game!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break
        
        if attempts == 0:
            print("Out of attempts! The word was:", word_to_guess)
            break
        
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess.")
            guessed_letters.append(guess)
            attempts -= 1
            print("Attempts remaining:", attempts)

if __name__ == "__main__":
    main()
