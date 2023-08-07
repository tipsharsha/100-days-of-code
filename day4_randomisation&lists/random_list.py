import random
names_given = input("Give names with a ,")
names = names_given.split(",")
print(random.choice(names))