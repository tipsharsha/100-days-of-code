"""This is a file for checking"""

#secret bidding
bids = {}
START = "yes"
while START == "yes":
    bids[input("What is your name? please")] = int(input("What is your bidding?"))
    start = input("Would you like to continue? (yes) or (no)")
MAX = ['list',0]
for bid,bit in bids:
    if bit > MAX[1]:
        MAX[0] = bid
        MAX[1] = bids[bid]

print(MAX[0],bids[MAX[0]])
