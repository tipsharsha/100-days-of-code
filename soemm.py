n = input("what is the number : ")
sum = 0
for digit in str(n):
    sum += int(digit)**len(n)
print(str(sum))
print(n)
print(n  == sum)