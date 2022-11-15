from blind_auction_art import logo
import os
clear = lambda: os.system('cls')

print(logo)
print("Welcome to the secret auction program!")
auction = {}
auction["name"] = []
auction["bid"] = []

others = True

while others:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))

    auction["name"].append(name)
    auction["bid"].append(bid)

    other_bidder = input("Are there any other biddes? Type 'yes' or 'no'. \n").lower()
    
    if other_bidder == 'yes':
        others = True
        clear()
    else: 
        others = False
        clear()

max_bid = max(auction["bid"])
index = auction["bid"].index(max_bid)
max_bidder = auction["name"][index]

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")