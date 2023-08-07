"""This behaves like a normal coffee machine in offices"""
# TODO: 1.First make variables for the resources available and profit made
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
PROFIT = 0
IS_ON = True


# TODO: 2.make a while loop which asks user for input so he can get his coffee
def process_coins(x):
    """describes the whole processs"""
    global PROFIT
    u = int(input("how many dimes did you put in")) * 0.05 + int(
        input("how many quarters did you put in")) * 0.25 + int(input("how many pennies did you put in")) * 0.01
    if MENU[x]["cost"] < u:
        PROFIT += u
        return 1
    else:
        return 0


def process_order(x):
    global resources
    for ingredient in MENU[x]["ingredients"]:
        if MENU[x]["ingredients"][ingredient] > resources[ingredient]:
            resources[ingredient] -= MENU[x][ingredient]
        else:
            return 0
    return 1


def greet(x):
    print(f"Enjoy your {x}! ☕☕☕")


while IS_ON:
    response = input("What would you like? (espresso/latte/cappuccino):")
    if response == "report":
        print(f"Left resources are {resources} and profit made is {PROFIT}")
    elif response == "off":
        IS_ON = False
    else:
        coins = process_coins(response)
        order = process_order(response)
        if coins and order:
            greet(response)
        elif coins:
            print("The order couldn't be processed cause money provided is not sufficient")
        else:
            print("We don't have the ingredients to make this order")

# TODO : 3.make a function to evaluate resources for given order

# TODO : 4.make a function to print out the given order to make coffee
# TODO : 5.print report if asked for report
# TODO :  6.turn off coffee machine when it is said to stop
# TODO : 7.make a function to process all the coins the customer put in
# TODO : 8. see transaction success
