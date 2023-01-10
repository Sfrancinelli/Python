student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("Udemy/26-day/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#TODO 1:
nato_dict = {row.letter : row.code for (index, row) in data.iterrows()}

print(nato_dict)

#TODO 2:
user_word = input("Enter your word:\n").upper()

code_input = [nato_dict[letter] for letter in user_word]

# for letter in nato_dict:
#     if letter in user_word:
#         code_input.append(nato_dict[letter])

print(code_input)
