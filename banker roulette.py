import random

names_string = input("Enter all family members name separated by comma and space:  ")
names = names_string.split(", ")

name = len(names)
rand = random.randint(0, name - 1)

print(f"{names[rand]} is going to buy the meal today!")
