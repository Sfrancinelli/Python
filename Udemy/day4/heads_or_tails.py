import random

start = input("Want to flip a coin? type 'Y' or 'N'\n").lower()
coin = random.randint(0,1)

if start == "y":
    if coin == 0:
        print("Heads")
    elif coin == 1:
        print("Tails")
    else: 
        print("Please flip the coin")
else:
    print("You didn't want to flip a coin :cn")




