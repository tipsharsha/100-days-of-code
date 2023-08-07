""""amma"""
import random

with open("Mail+Merge+Project+Start/Input/Letters/starting_letter.txt") as letter:
    let = letter.read()
with open("Mail+Merge+Project+Start/Input/Names/invited_names.txt") as names:
    nam = names.read()
    name = nam.split('\n')

with open("message.txt","a") as message:
    for names in name:
        new_let = let
        new_let = new_let.replace("[name],",names)
        print(new_let)
