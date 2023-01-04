import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level (displays the password with letters, symbols, and numbers in this order)
# password = ""

# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for sym in range(1, nr_symbols + 1):
#     random_sym = random.choice(symbols)
#     password += random_sym

# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num

# print(f"Your new generated password is {password}")

# displays completely random passwords all the time
password = []

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    password.append(random_char)

for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    password.append(random_sym)

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password.append(random_num)

random.shuffle(password)

random_pass = ""

for char in password:
    random_pass += char

print(f"Your new generated password is {random_pass}")


