import random
hand = ["rock","paper","scissors"]
x = (input("What do you choose   ")).lower()
chosen = hand.index(x)
print(f"You have chosen {x}")
randal = random.randint(0,2)
y = hand[randal]
print(f"computer has chosen {y}")
if (chosen == 0 and randal == 1) or (chosen == 1 and randal == 2) or (chosen == 2 and randal == 0):
    print("You have lost and computer has won.")
elif chosen == randal:
    print("Nobody won or lost the game.")
else:
    print("You have won the game and computer lost.")