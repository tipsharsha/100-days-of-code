"""Black Jack game"""
import random
cards = [11,10,10,10,10,2,3,4,5,6,7,8,9]

def deal_card():
    """Deals one card"""
    return random.choice(cards)

ur_cards = []

computer_cards =[]

for i in range(2):
    ur_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

