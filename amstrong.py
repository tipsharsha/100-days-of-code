n = input("what is the number : ")
sum = 0
for digit in str(n):
    sum += int(digit)**3
if sum == int(n):
    print("amstrong number")
else:
    print("not an armstrong number")