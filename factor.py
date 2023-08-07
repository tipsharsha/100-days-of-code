x = input("number you need factors for")
i = 1
for i in range (1,int(x)+1):
    if int(x)%i == 0:
        print(str(i))
    i += 1