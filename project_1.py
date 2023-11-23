####guess the number #####

import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    secret_number = random.randint(1,100)
    print(secret_number)

    attempts = 0

    while True:

        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts")
        elif guess < secret_number:
            print(f"Too low! Try again.")
        else:
            print(f"Too high! Try again")

number_guessing_game()
