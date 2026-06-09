# Number Guessing Game


print("----NUMBER GUESSING GAME----")

print("Enter some details to begin:")
name = input("Full Name: ")
age = int(input("Age: "))
education = input("Your Education: ")

print("Lets start the game")

import random

num = random.randint(1, 50)
tries = 0

while True:
    guess = int(input("Guess any number between 1 - 50: "))
    if num == guess:
        tries += 1
        print(f"You guessed a correct number in {tries} tries")
        break
    elif num > guess:
        tries += 1
        print("Try a little bigger number")
    elif num < guess:
        tries += 1
        print("Try a little smaller number")
    else:
        print("You guessed wrong number, Please Try Again!")
    if tries == 5:
        print("You have reached maximum attempts, please try your luck next time")
        print(f"By the way, the correct number was {num}")
        break
