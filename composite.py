import math
num = int(input("what is your number"))
flag = False
if num == 1:
      print("neither prime or composite")
if num>1:
    for i in range (1 , num**0.5):
        if num%i == 0:
            flag = True
if flag:
    print("this is a not prime number")
else:
    print("this is a prime number")