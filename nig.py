x = input("what is the string : ")
list1 = []
list2 = []
for i in range(0, len(x)+1):
    for y in range(i+1, len(x)+1):
        list1.append(x[i:y])
for i in range(len(list1)):
    if list1[i] == list1[i][::-1]:
        list2.append(list1[i])
res = max(list2, key=len)
print(res)