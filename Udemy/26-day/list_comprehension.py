# How to create a list from another list in Python
# We usually used for loops to create em, but there's a method:

number = [1, 2, 3]
new_list = []

for n in number:
    add_1 = n + 1
    new_list.append(add_1)

# New method:
# The new_item, item and list variables are there so the "new_list" doesn't need show any errors.
new_item = "x"

item = "y"

list = []

test = "Condición"

# This is called list comprehension and is an unique tool of Python for making list from another list.
new_list = [new_item for item in list]

# So, from the example in the first lines, it would be something like this:
new_list = [n + 1 for n in number]

print(new_list) # [2, 3, 4]

# This can be done with strings as well:
name = "Angela"

letters_list = [letter for letter in name]
 
print(letters_list)

rango = range(1,5)

rango_x2 = [r * 2 for r in rango]

print(rango_x2)

# There's also a step forward in this mechanic called "Conditional List Comprehension".
# This works just like the examples above but requires the verification of a condition. Ej:
# It will only execute the code if the condition is passed.

new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Adding names to another list if the len is lesser than 5
short_names = [name for name in names if len(name) < 5]

print(short_names)

# Changing names to uppercase if len greater than 5
upper_long_names = [name.upper() for name in names if len(name) > 5]

print(upper_long_names)

# List comprehension exercise: Create a new list containing every number in the list
# Numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n ** 2 for n in numbers]

print(squared_numbers)

# Exercise n 2: Create a new list called result. This new list should only
# contain the even numbers from the list numbers:

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [n for n in numbers if n % 2 == 0]

print(result)


# Exercise n 3: Take a look inside file1.txt and file2.txt. They each contain
# a bunch ofnumbers, each number in a new line.
# You are going to create a list called "common_nums" which contains the numbers
# that are common in both files

with open("Udemy/26-day/file1.txt") as file_1:
    nums_1 = file_1.readlines()

with open("Udemy/26-day/file2.txt") as file_2:
    nums_2 = file_2.readlines()

nums1 = [int(n) for n in nums_1]
nums2 = [int(n) for n in nums_2]

common_nums = [n for n in nums1 if n in nums2]
print(common_nums)