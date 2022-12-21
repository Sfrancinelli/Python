class Coffee_machine:
    def __init__(self, menu, money, resources):
        self.menu = menu
        self.money = money
        self.resources = resources


    def __str__(self):
        return f"The menu is {list(self.menu.keys())}. Money and resources can get accesed via 'report' input."


    def off(self):
        """Turns off the coffee machine."""
        return "Machine turning off."
    

    def report(self):
        """Breaks down the report feature to make it more readable"""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")


    def resource_check(self, order_ingredients):
        """Returns True when order can be made, and False when resources are insufficient"""
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("How many quarters?:")) * 0.25
        total += int(input("How many dimes?:")) * 0.1
        total += int(input("How many nickles?:")) * 0.05
        total += int(input("How many pennies?:")) * 0.01
        return total


    def is_transaction_successful(self, money_received, drink_cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.money += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False


    def make_coffee(self, drink_name, order_ingredients):
        """Deduct the required ingredients from the resources."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}. Enjoy it!")


menu = {
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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine = Coffee_machine(menu, money, resources)

print(coffee_machine)

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print(coffee_machine.off())
        is_on = False
    elif choice == "report":
        coffee_machine.report()
    else:
        drink = menu[choice]
        if coffee_machine.resource_check(drink["ingredients"]):
            payment = coffee_machine.process_coins()
            if coffee_machine.is_transaction_successful(payment, drink["cost"]):
                coffee_machine.make_coffee(choice, drink["ingredients"])



