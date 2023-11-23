import random

def choose_word():
    words = ["python", "java", "programming", "code", "computer", "algorithm", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def word_guessing_game():
    print("Welcome to the word guessing game!!!")

    secret_word = choose_word()

    guessed_letters = set()

    max_attempts = 6
    incorrect_attempt = 0

    while incorrect_attempt < max_attempts:
        current_display = display_word(secret_word, guessed_letters)
        print(f"current word: {current_display}")

        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed that letter. try again.")

        guessed_letters.add(guess)

        if guess not in secret_word:
            incorrect_attempt += 1
            print(f"Incorrect guess! {max_attempts - incorrect_attempt} attempts")
        
        if set(secret_word) == guessed_letters:
            print(f"Congratulations! you guessed the word: {secret_word}")
            break
        
    if incorrect_attempt == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct word was: {secret_word} ")

word_guessing_game()


