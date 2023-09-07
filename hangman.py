import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "giraffe", "hamburger", "iguana", "jacket", "kangaroo", "lemon", "monkey", "nachos", "octopus", "penguin", "quokka", "rhinoceros", "strawberry", "tiger", "umbrella", "vampire", "watermelon", "xylophone", "yacht", "zeppelin"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_random_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while True:
        print("\nAttempts left:", attempts)
        display = display_word(word, guessed_letters)
        print(display)

        if display == word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

            if attempts == 0:
                print("Game over! The word was:", word)
                break

if __name__ == "__main__":
    hangman()
