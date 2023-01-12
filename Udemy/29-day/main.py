from tkinter import *
import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    global password

    for char in range(1, random.randint(0, len(LETTERS) -1)):
        random_char = random.choice(LETTERS)
        password.append(random_char)

    for sym in range(1, random.randint(0, len(SYMBOLS) -1)):
        random_sym = random.choice(SYMBOLS)
        password.append(random_sym)

    for num in range(1, random.randint(0, len(NUMBERS) -1)):
        random_num = random.choice(NUMBERS)
        password.append(random_num)

    random.shuffle(password)

    random_pass = ""

    for char in password:
        random_pass += char

    pass_entry.insert(END, random_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    with open("Udemy/29-day/data.txt", "w") as data:
        data.write(f"{website} | {email} | {password}")

# ---------------------------- UI SETUP ------------------------------- #
# Root
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.grid_rowconfigure(0, weight=2)

# Canvas Image
canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="Udemy/29-day/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entrys
web_entry = Entry(width=53)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
# Pre populated field
email_entry.insert(0, "sebastianfrancinelli00@gmail.com") 

pass_entry = Entry(width=34)
pass_entry.grid(column=1, row=3, columnspan=1)

# Buttons
add_btn = Button(text="Add", command=add, justify="center", width=44)
add_btn.grid(column=1, row=4, columnspan=2)

generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(column=2, row=3, columnspan=1)

window.mainloop()