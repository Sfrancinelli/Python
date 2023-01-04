from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        winner = "a"
    elif b_followers > a_followers:
        winner = "b"
    if guess == winner:
        return True
    else:
        return False

score = 0
print(logo)
game_continue = True
clear = lambda: os.system('cls')

account_b = random.choice(data)

while game_continue:

    account_a = account_b #Para poner la opcion b en "A" y que siempre haga eso
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else: 
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")




