"""plays the higher and lower game"""
# import Random and other data files
# import clear function
import random
from os import system
from  art import LOGO,VS
from game_data import data
#print our logo
print(LOGO)
#TO-DO: 1.make this file a python file
def clear():
    """clears the screen"""
    system('cls')
COUNT = 0
#create a count variable to keep the count
FLAG = True
#create a condition so that the loop runs
A = random.choice(data)
B = random.choice(data)
while FLAG:
    # take a random A and B to compare
    A = B
    B = random.choice(data)
    #print out the celebrities
    print(f"Compare A: {A['name']},a {A['description']}, from {A['country']}")
    print(VS)
    print(f"Compare B: {B['name']},a {B['description']}, from {B['country']}")
    #make user guess who is more popular
    x = input("who has more followers? A or B:  ")
    if x == "A":
        GUESS = A
    else:
        GUESS = B
    COUNT += 1
    FLAG = (GUESS['follower_count'] == max(A['follower_count'],B['follower_count']))

    #Give the guy some appreciation
    clear()
    print(LOGO)
    if FLAG:
        print(f"You are right! Current score: {COUNT}")
print(f"Sorry that's wrong, Final score {COUNT-1}")
