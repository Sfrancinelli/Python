import random
import os
from blackjack_art import logo
clear = lambda: os.system('cls')

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and calculates the score and the blackjack. Changes the value of the 'ace' from 11 to 1 if the score passes the 21 mark."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []

computer_cards = []

is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

