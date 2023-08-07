list = [1,2,3]
sublists = []
for i in range(len(list)+1) :
    for j in range(i):
        sublists.append(list[j:i])
maximae = []

for i in range(len(sublists)):
    sublists[i].sort()
    maximae.append(sublists[i][-1]) 
print(sublists)
maximae.sort()
print(maximae)

print("maximum of the sublists is "+ str(maximae[-1]))
y=0
for x in range(len(maximae)):
    if maximae[x] == maximae[-1]:
        y+=1
print("maximum of the sublists has occured "+ str(y) +" times")