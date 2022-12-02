from game_data import data
#len of data = 50
from art import logo, vs
import random

ran_number = random.randint(0,50)
print(logo)
score = 0

value = data[ran_number]
value2 = data[random.randint(0,50)] 

def compare():
    if value['follower_count'] > value2['follower_count']:
        winner = "A"
    elif value2['follower_count'] > value['follower_count']:
        winner = "B"
    return winner

winner = compare()

def result(answer):
    score = 0
    global end_game
    if answer == winner:
        print(f"You're right! Current score: {score}")
        end_game = False
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_game = True
    return end_game
 
def string_to_show1(dic):
    return f"{dic['name']}, a {dic['description']}, from {dic['country']}"

def string_to_show2(dic):
    return f"{dic['name']}, a {dic['description']}, from {dic['country']}"
    
final_string1 = string_to_show1(value) 
final_string2 = string_to_show2(value2)

print(f"Compare A: {final_string1}")
print(vs)
print(f"Against B: {final_string2}")
answer = input("Who has more followers? Type 'A' or 'B': ").upper
end_game = result(answer)

while not end_game:
    print(f"Compare A: {final_string1}")
    print(vs)
    print(f"Against B: {final_string2}")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper
    end_game = result(answer)