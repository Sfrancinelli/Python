from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    countdown(1500)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count -1)
       
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Udemy/28-day/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start, justify="right")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, justify="left")
reset_button.grid(column=2, row=2)

check = Label(text=CHECK_MARK*3, fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)


window.mainloop()