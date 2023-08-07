import random

from wcwidth import list_versions

from hangman_art import art,stages

from hangman_words import word_list

print(art)
lives = 6
the_word = random.choice(word_list)
word = []
for world in the_word:
    word += world
print(the_word)
print(word)
until_guessed = []
for c in range(len(the_word)):
    until_guessed += "_"
guesses = []
print(until_guessed)
while lives and (until_guessed != word) :

    user_input = input("Guess a word :")

    if (user_input in the_word) and (user_input not in guesses):
        for location in range(0,len(the_word)):
            if the_word[location] == user_input:
                until_guessed[location] = user_input
        print(until_guessed)
        print(f"you have {lives} lives left")
        print(stages[lives])    
    elif user_input in guesses:
        print("You have already guessed this letter.")
        print(until_guessed)
        print(f"you have {lives} lives left")
        print(stages[lives])     
    else:
        lives -= 1
        print(until_guessed)
        print(f"you have {lives} lives left")
        print(stages[lives])
        
    guesses += user_input
if until_guessed != word:
    print("You have lost the game.")
else:
    print("You have won the game.")
