rows = int(input("number of rows :"))
columns = int(input("number of columns :"))
matrix_a = []
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix_a.append(a)
temp = []
trans = []
x = 1
y = 1
while x <= columns:
    temp.append(0)
    x += 1
while y <= rows:
    trans.append(temp)
    y += 1
print(trans)
for i in range(columns):
    for j in range(rows):
        trans[i][j] = matrix_a[j][i]
for r in trans:
    print(r)
if trans == matrix_a:
    print("Its symm")
else:
    print("non sym")
