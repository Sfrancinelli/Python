from tkinter import *
import pandas
import math
import random
from functools import partial

BACKGROUND_COLOR = "#B1DDC6"
language = "French"

# ---------------------------- CSV READINFG ----------------------------

data_frame = pandas.read_csv("Udemy/31-day/data/french_words.csv")

data = data_frame.to_dict(orient="records")

print(data[0]['French']) # Format to acces french words

print(data[0]['English'])

print(len(data)) # 101

# ---------------------------- TIMER --------------------------------

def countdown(count):
    """Counts the number of seconds especified by the parameter (count) and changes the text of the canvas"""
    count_min = math.floor(count / 60)

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
        if count % 3 == 0:
                change_word('french')
                print("changing")

# ---------------------------- Change Word ----------------------------

def change_word(languague):
    """Changes the word of the canvas for another random one. The input language has to be in lowercase"""
    
    random_num = random.randint(0,100)

    if languague == "english":
        english_word = data[random_num]['English']
        print(english_word)
        canvas.itemconfig(word_text, text=english_word)
    elif languague == "french":
        french_word = data[random_num]['French']
        print(french_word)
        canvas.itemconfig(word_text, text=french_word)

# ---------------------------- UI INTERFACE ----------------------------

# function_french = change_word("french")
# function_english = change_word("english")

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

word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

# Buttons
cross_image = PhotoImage(file="Udemy/31-day/images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=partial(change_word, "english"))
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="Udemy/31-day/images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=partial(change_word, "french"))
tick_button.grid(row=1, column=1)

# countdown(300)

window.mainloop()
