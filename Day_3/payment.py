#nested if statement
height = int(input("What is your height "))
age = int(input("What is your age   "))
if height>120:
    if age > 18:
        print("Please pay $12")
    elif age <18 and age >12:
        print("Please pay $7")
    else :
        print("Please pay $5")
else :
    print("Sorry kid! you have to grow taller")