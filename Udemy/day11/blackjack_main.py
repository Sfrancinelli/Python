import random
from blackjack_art import logo
import os
clear = lambda: os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []

dealer = []

user_score = 0

dealer_score = 0

reset = True

def deal_cards(num,player):
    """Return a random card from the deck and give it to both the player and dealer."""
    if num == 2:
        for i in range(2):
            user.append(cards[random.randint(0,12)])
            dealer.append(cards[random.randint(0,12)])
    elif num == 1 and player == "user":
        user.append(cards[random.randint(0,12)])
    elif num == 1 and player == "dealer":
        dealer.append(cards[random.randint(0,12)])

def keep_score():
    """Evaluates the score of the players and defines a winner."""
    global user_score
    global dealer_score
    if not has_blackjack():
        user_score = sum(user)
        if user_score > 21:
            if 11 in user:
                user.remove(11)
                user.append(1)
                user_score = sum(user)
            elif 11 not in user:
                print("You lose!")
                print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")
        dealer_score = sum(dealer)
        if dealer_score > 21 and user_score < 21:
            if 11 in dealer:
                dealer.remove(11)
                dealer.append(1)
                dealer_score = sum(dealer)
                keep_score()
            elif 11 not in dealer:
                print("You won!")
                print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")
        elif dealer_score <= 17:
            deal_cards(1,"dealer")
            print("Computer drew a card")
            keep_score()

def has_blackjack():
    """Evaluates if any player got a blackjack. Returns true if they've got a blackjack and prints the result."""
    if user == [11,10] or user == [10,11]:
        print("You got a blackjack! You win!")
        return True
    elif dealer == [11,10] or dealer == [10,11]:
        print("Computer got a blackjack, you lose!")
        return True
    else:
        return False

def restart():
    """Restarts the console, the scores and the game itself."""
    global user
    global dealer
    global user_score
    global dealer_score
    clear()
    user = []
    dealer = []
    user_score = 0
    dealer_score = 0

while reset:

    restart()
    print(logo)

    deal_cards(2,"any")
    keep_score()
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {dealer[0]}")

    if not has_blackjack():

        while user_score < 21 and dealer_score < 21:
            continuar = input("Do you want another card? Type 'y' to continue drawing or 'n' to keep your score. \n").lower()
            if continuar == 'y':
                deal_cards(1,"user")
                print(f"User: {user}")
                keep_score()
                print(f"User score: {user_score}")
                print(f"Computer's first card: {dealer[0]}")
            if continuar == 'n':
                keep_score()
                if user_score > dealer_score:
                    print("You win!")
                    print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")
                elif dealer_score > user_score:
                    print("Computer wins!")
                    print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")
                elif user_score == dealer_score:
                    print("It's a draw! Both players draw a card!")
                    deal_cards(1,"user")
                    deal_cards(1,"dealer")
                    print(f"user: {user}")
                    print(f"dealer: {dealer}")
                    keep_score()
                    print(f"User score: {user_score}")
                    print(f"Computer score: {dealer_score}")
                break

    if user_score == 21 and dealer_score != 21:
        print("You win!")
        print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")
    elif dealer_score == 21 and user_score != 21:
        print("You lose!")
        print(f"Computer's score was: {dealer_score}, and computer's hand was {dealer}")

    new_game = input("Would you like to restart the game? Type 'y' to continue playing or 'n' to stop!. \n").lower()
    if new_game == 'y':
        reset = True
    if new_game == 'n':
        reset = False

print("Goodbye!")



    