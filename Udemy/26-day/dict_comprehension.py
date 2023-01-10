import random
# Dictionary Comprehension sintaxis:

new_key = "key"
new_value = "value"
item = "item"
iterable = []
dict = {}
test = "if statement"

# Ignore the above code, made it so it doesn't throw an error.
new_dict = {new_key : new_value for item in iterable if test}

new_Dict = {new_key : new_value for (key, value) in dict.items() if test}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student:random.randint(1,100) for student in names}

print(students_scores)

passed_students = {student:value for (student, value) in students_scores.items() if value >= 60}

print(passed_students)

# Exercise 1: Use dict comprehension to create a dictionary called "result"
# That takes each word in the fiven sentence and calculates the number of letters
# in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

list_of_words = sentence.split()

result = {word : len(word) for word in list_of_words}

print(result)

# Exercise 2: 