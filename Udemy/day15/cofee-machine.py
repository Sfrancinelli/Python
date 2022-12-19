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
}