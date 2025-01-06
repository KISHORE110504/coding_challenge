import random

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
chosen_word =random.choice(word_list)

guess = input("Guess the word:").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")