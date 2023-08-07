def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


nu1 = input("give your first number : ")
nu2 = input("giveyour second number : ")
nu3 = input("Give your last number : ")
print(max_num(nu1, nu2, nu3))
