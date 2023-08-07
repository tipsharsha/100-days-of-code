import random
print("Welcome to random password generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
lette = int(input ("How many letters do you need?"))
sp_char = int(input ("How many sp chars do you need?"))
numbe = int(input("How many numbers do you want in your password?"))
my_list =[]
for number in range(0,numbe):
    my_list.append(random.choice(numbers))
for number in range(0,lette):
    my_list.append(random.choice(letters))
for number in range(0,sp_char):
    my_list += random.choice(symbols)
random.shuffle(my_list)
password = ""
for list in my_list:
    password += list
print("Your password could be "+password)