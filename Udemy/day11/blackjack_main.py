import random
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []

dealer = []

user_score = 0

dealer_score = 0

def deal_cards(num,player):
    if num == 2:
        for i in range(2):
            user.append(cards[random.randint(0,12)])
            dealer.append(cards[random.randint(0,12)])
    elif num == 1 and player == "user":
        user.append(cards[random.randint(0,12)])
    elif num == 1 and player == "dealer":
        dealer.append(cards[random.randint(0,12)])
    has_blackjack()

def keep_score():
    global user_score
    global dealer_score
    user_score = sum(user)
    if user_score > 21:
        if 11 in user:
            user.remove(11)
            user.append(1)
            user_score = sum(user)
        elif 11 not in user:
            print("You lose!")
    dealer_score = sum(dealer)
    if dealer_score > 21 and user_score < 21:
        if 11 in dealer:
            dealer.remove(11)
            dealer.append(1)
            dealer_score = sum(dealer)
            keep_score()
        elif 11 not in dealer:
            print("Dealer lose!")
    elif dealer_score <= 17:
        deal_cards(1,"dealer")
        print(f"dealer: {dealer}")
        print(f"Computer score: {dealer_score}")
        keep_score()

def has_blackjack():
    if user == [11,10] or user == [10,11]:
        print("You got a blackjack! You win!")
    elif dealer == [11,10] or dealer == [10,11]:
        print("Computer got a blackjack, you lose!")

print(logo)

deal_cards(2,"any")
print(f"user: {user}")
print(f"dealer: {dealer}")
keep_score()
print(f"User score: {user_score}")
print(f"Computer score: {dealer_score}")
while user_score < 21 and dealer_score < 21:
    continuar = input("Do you want another card? Type 'y' to continue drawing or 'n' to keep your score. \n").lower()
    if continuar == 'y':
        deal_cards(1,"user")
        print(f"User: {user}")
        keep_score()
        print(f"User score: {user_score}")
        print(f"Computer score: {dealer_score}")
    if continuar == 'n':
        keep_score()
        if user_score > dealer_score:
            print("You win!")
        elif dealer_score > user_score:
            print("Dealer wins!")
        elif user_score == dealer_score:
            print("It's a draw! Both players draw a card!")
            deal_cards(1,"user")
            deal_cards(1,"dealer")
            keep_score()
            print(f"User score: {user_score}")
            print(f"Computer score: {dealer_score}")
if user_score == 21 and dealer_score != 21:
    print("You win!")


    