# FileNotFound
# with open("a_file.txt") as file:
#   file.read()


# KeyError
# a_dictionary = {"key" : "value"}
# print(a_dictionary["non_existent_key"])

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# FileNotFound Handling
try:
    my_file = open("Udemy/30-day/a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    my_file = open("Udemy/30-day/a_file.txt", "w")
    my_file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
# The else block will be executed if the code goes without errors
else:
    content = my_file.read()
    print(content)
# The finally block will be executed no matter what happens to the code above!
finally:
    print("This will happen no matter what!")
    my_file.close()

# The Raise Keyword will raise an error of your choice! Ej:
# try:
#     text = "abc"
#     print(text + 5)
# finally:
#     raise IndexError


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters!")

bmi = weight/height**2
print(bmi)