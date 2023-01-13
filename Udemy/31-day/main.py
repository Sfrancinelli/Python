from tkinter import *
import pandas
import math

BACKGROUND_COLOR = "#B1DDC6"
language = "French"
word = "something for now"

# ---------------------------- CSV READINFG ----------------------------

data_frame = pandas.read_csv("Udemy/31-day/data/french_words.csv")

data = data_frame.to_dict(orient="records")

print(data)

# ---------------------------- TIMER --------------------------------

def countdown(count):

    global check_mark_multiplier

    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start()
        if reps % 2 == 0:
            check.config(text=f"{CHECK_MARK*check_mark_multiplier}")
            check_mark_multiplier += 1
       

# ---------------------------- UI INTERFACE ----------------------------

# Root
window = Tk()
window.title("Flash Card Proyect")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
canvas_img_front = PhotoImage(file="Udemy/31-day/images/card_front.png")

canvas_img_back = PhotoImage(file="Udemy/31-day/images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=canvas_img_front)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text
title_text = canvas.create_text(400, 150, text=language, fill="black", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text=word, fill="black", font=("Ariel", 60, "bold"))

# Buttons
cross_image = PhotoImage(file="Udemy/31-day/images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="Udemy/31-day/images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0)
tick_button.grid(row=1, column=1)


window.mainloop()
