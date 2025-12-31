from art import logo
import random

def number_guess(attempts):
    game_over = False
    while not game_over and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess < target_number:
            print("Too low. \nGuess again.")
            attempts -= 1
            continue
        elif guess > target_number:
            print("Too high. \n Guess again.")
            attempts -= 1
            continue
        else:
            print(f"You got it! The answer is {target_number}")
            game_over = True
    if attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard':")
attempts = 0
target_number = random.randint(1, 100)

if choice == "easy":
    attempts += 10
else:
    attempts += 5

number_guess(attempts)
