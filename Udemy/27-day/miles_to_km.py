from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=80)
window.config(padx=10, pady=10)

nothing = Label(text="")
nothing.grid(column=0, row=0)

entry_miles = Entry(width=15)
entry_miles.insert(END, string="0")
entry_miles.focus()
entry_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

entry_km = Label(width=15, text="0")
entry_km.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)


def calculate():
    miles = entry_miles.get()
    km = round(float(miles) * 1.609, 2)
    entry_km.config(text=km)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row= 2)

window.mainloop()