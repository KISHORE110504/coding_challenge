import random
from game_data import data
import art

def format_data(account):
  """Takes the account data and returns the printable format."""
    return (f"{account["name"]}, a {account["description"]}, from {account["country"]}")

def check_answer(user_guess, personality_1, personality_2):
  """Take a user's guess and the follower counts and returns if they got it right."""
    if personality_1["follower_count"] > personality_2["follower_count"]:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

score = 0
game_over = False
personality_2 = random.choice(data)

while not game_over:
    personality_1 = personality_2
    personality_2 = random.choice(data)

    if personality_1 == personality_2:
        personality_2 = random.choice(data)

    print(f"Compare A: {format_data(personality_1)}")
    print(art.vs)
    print(f"Against B: {format_data(personality_2)}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(art.logo)

    is_correct = check_answer(choice, personality_1, personality_2)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
