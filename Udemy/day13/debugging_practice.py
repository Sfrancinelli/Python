############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# The range function, does not include the B argument, so it will never get to the value = 20.

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# The list index goes from 0 to 5, so the randint generator should also go from 0 to 5 (it does include both arguments)

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# This code does not include years before 1980 (including 1980) and also doesn't include the year 1994!

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print(f"You can drive at age {age}.")

# If you don't convert the data type to integer or float, it wont be possible to do mathematical comparisons :/. Also, the print statement aint indented so it will cause an error.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# The doble '=' sign is wrong. That's used to compare elements and not to asign values.

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])

# The indentation on line 51 it's worng (considering the purpose of the function). Needs to be inside de for loop to multiply all the values of the list.