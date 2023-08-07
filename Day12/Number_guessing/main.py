"""A number guessing game"""
import random

print("Welcome to the guessing game! \n I am thinking of a number between 1 and 100")

DIFF = input("Choose a difficulty hard or easy  ")
NUMB = random.randint(0,100)

if DIFF == "hard":
    ATTEMPTS = 5
else:
    ATTEMPTS = 10
def play_game():
    """Helps play game"""
    global ATTEMPTS
    guess = -1
    while ATTEMPTS != 0 and guess != NUMB:
        print(f"You have {ATTEMPTS} attempts remaining")
        guess = int(input("give your guess:  "))
        if guess > NUMB:
            print("go lower")
        elif guess < NUMB:
            print("go higher")
        ATTEMPTS -= 1

    return guess

x = play_game()
if x == NUMB:
    print("You have guessed the game successfully")
elif ATTEMPTS == 0:
    print("You have lost")
