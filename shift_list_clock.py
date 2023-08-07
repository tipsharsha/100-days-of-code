list = []
list1 = []
c = int(input("number of rotations"))
Flag = True 
while Flag:
    x = input("element to add:")
    if x == "stop":
        Flag = False
    else:
            list.append(x)
for i in range (-c,len(list)-c):
    list1.append(list[i])
print(list1)