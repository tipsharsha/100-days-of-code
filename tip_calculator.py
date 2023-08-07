print("Welcome to the tip generator")
bill = float(input("What was the bill total? $"))
tip_per = int(input("How much percentage tip would you like to give? 10,12 or 15?   "))
no_ppl = int(input("How many people to spilt the bill   "))
total = ((100 + tip_per)/100)*(bill)
per_person = total/no_ppl
print(round(per_person,2))
final_amount = "{:.2f}".format(per_person)
print(final_amount)