from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Ads padding to the window
window.config(padx=20, pady=20)

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# Add padding on the label
my_label.config(padx=30, pady=30)

# The place method is completely specific because it requires the x and y parameters
# It turn into a bit of a nightmare if you have many many widgets
# Very much like CSS:

# my_label.place(x=100, y=200)

# There's also de GRID method, wich workd quite similar to CSS:

my_label.grid(column=0, row=0)


button = Button(text="Click Me")
button.grid(column=1, row=1)

entry = Entry(width=10)
entry.grid(column=3, row=2)

# Grid and Pack are uncompatible

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

window.mainloop()