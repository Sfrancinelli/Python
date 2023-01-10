import tkinter

window = tkinter.Tk()

window.title("First GUI")
window.minsize(width=500, height=300)

# Label creation
label = tkinter.Label(text="I am a Label", font=("Courier", 24, "italic"))
label.pack(expand=True)

window.mainloop()