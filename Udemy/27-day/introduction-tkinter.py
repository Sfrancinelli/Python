from tkinter import *

window = Tk()

window.title("First GUI")
window.minsize(width=500, height=300)

# Label creation
label = Label(text="I am a Label", font=("Courier", 24, "italic"))
label.pack()

# Update properties of a created object
label["text"] = "New text"
label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    # Get the label to display what's on the Entry
    label.config(text=input.get())

button = Button(text="Click ME", command=button_clicked)
button.pack()

# Entry 

input = Entry(width=10)
input.pack()
# Get the Entry input
print(input.get())


window.mainloop()