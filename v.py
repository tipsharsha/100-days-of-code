temp = []
trans = []
x=1
y=1
while x <= rows:
    temp.append(0)
    x += 1
while y <= columns:
    trans.append(temp)
    y += 1
print(trans)