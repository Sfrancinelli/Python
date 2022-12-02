from game_data import data
#len of data = 50
from art import logo, vs
import random

ran_number = random.randint(0,50)
print(logo)
score = 0

value = data[ran_number]
value2 = data[random.randint(0,50)]

def compare_A():
    pass

def string_to_show1(dic):
    return f"{dic['name']}, a {dic['description']}, from {dic['country']}"
    
final_string1 = string_to_show1(value)
print(final_string1)

def string_to_show2(dic):
    return f"{dic['name']}, a {dic['description']}, from {dic['country']}"
    
final_string2 = string_to_show2(value2)
print(final_string2)