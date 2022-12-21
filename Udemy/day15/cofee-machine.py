# 3 hot flavours: Espresso, Latte and Capuccino
# Espresso recipe: 50ml Water and 18g Coffee. Price $1.50
# Latte recipe: 200ml Water, 24g Coffee and 150ml Milk. Price $2.50
# Capuccino recipe: 250ml Water, 24g Coffee and 100ml Milk. Price $3.00
# American coins: Penny = 1cent ($0,01), Nickel = 5cents ($0,05), Dime = 10cents ($0,10), Quarter = 25cents ($0,25)
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
    "money": 0
}
# print(MENU["cappuccino"]["ingredients"]["water"])
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return round(total, 2)


def report(input):
    if input == "report":
        return f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money: {resources["money"]}
        """


def coffee_machine(input, resources):
    """Gets the choice of the user and the resources of the machine and returns the coffee if enough resources."""
    if input == "report":
        return report(input)
    if input == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif input == "capuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    elif input == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    if resources["water"] < 0:
        return "Sorry there is not enough water."
    elif resources["coffee"] < 0:
        return "Sorry there is not enough coffee."
    elif  resources["milk"] < 0:
        return "Sorry there is not enough milk."   
    return process_coins()


def transaction(choice, money):
    if choice == "espresso":
        drink_cost = MENU["espresso"]["cost"]
    elif choice == "capuccino":
        drink_cost = MENU["cappuccino"]["cost"]
    elif choice == "latte":
        drink_cost = MENU["latte"]["cost"]
    if money == drink_cost:
        return f"Enjoy your {choice}!"
    elif money > drink_cost:
        change = round(money - drink_cost, 2)
        return f"Here is ${change} in change. Enjoy your {choice}!"
    elif money < drink_cost:
        return "Sorry that's not enough money. Money refunded."


want = input("What would you like? (espresso/latte/cappuccino/report): ").lower()

coffee = coffee_machine(want, resources)
print(coffee)
if want != "report":
    transaccion = transaction(want, coffee)
    print(transaccion)

