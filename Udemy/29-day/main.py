from tkinter import *
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    pass
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.grid_rowconfigure(0, weight=2)


canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="Udemy/29-day/logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

add_btn = Button(text="Add", command=add, justify="center", width=43)
add_btn.grid(column=1, row=4, columnspan=2)

web_entry = Entry(width=45)
web_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

pass_entry = Entry(width=31)
pass_entry.grid(column=1, row=3, columnspan=1)

generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(column=2, row=3, columnspan=1)

window.mainloop()