x = input("what is the string : ")
flag = False
for i in range (len(x)):
	for y in range (i,len(x)):
		for u in range (y-i):
			if x[i+u] == x[y-u]:
				flag = True
	if flag:
		print(x[i:y])       