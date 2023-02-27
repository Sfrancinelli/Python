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

# Exercise 2: Use dictionary comprehension to create a dict called weather_f
# that takes each temperature in degrees Celcius and converts it into Farenheight

weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}

weather_f = {day : (temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)

student_dict = {
    "student" : ["Angela", "James", "Lilly"],
    "score" : [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Looping and using comprehension in pandas DataFrame
import pandas

student_data = pandas.DataFrame(student_dict)
print(student_data)

# Loop through a data frame:
for (key, value) in student_data.items():
    print(key)
    print(value)

# Loop through rows of a data frame:
for (index, row) in student_data.iterrows():
    print(index)
    print("------------")
    print(row)
    print("------------")
    print(row.student)
    print("------------")