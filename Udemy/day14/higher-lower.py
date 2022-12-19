from game_data import data
#len of data = 50
from art import logo, vs
import random
import os
clear = lambda: os.system('cls')

print(logo)
score = 0
value2 = random.choice(data) 
# Crear una funcion para que me genere numeros random, porque no está funcando
def game():
    global score 
    global ran_number
    global end_game
    global value2
    def random_number():
        number = random.randint(0,49)
        return number

    ran_number = random_number()

    value = value2
    value2 = data[random_number()]

    while value == value2:
        value2 = random.choice(data)

    # Arreglar la función compare, no está retornando los valores bien.
    def compare():
        winner = ""
        if value['follower_count'] > value2['follower_count']:
            winner = "A"
        elif value2['follower_count'] > value['follower_count']:
            winner = "B"
        return winner

    winn = compare()

    def result(answer):
        global score
        global end_game
        if answer == winn:
            score += 1
            print(f"You're right! Current score: {score}")
            end_game = False
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
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    end_game = result(answer)

    return end_game

end_game = game()

while not end_game:
    game()

    # if winn == "A":
    #     value = data[random_number()] 
    # elif winn == "B":
    #     value2 = data[random_number()]
    # final_string1 = string_to_show1(value) 
    # final_string2 = string_to_show2(value2)
    # print(f"Compare A: {final_string1}")
    # print(vs)
    # print(f"Against B: {final_string2}")
    # answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    # end_game = result(answer)