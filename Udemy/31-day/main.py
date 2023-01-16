from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
language_title = "French"
current_card = {}

# ---------------------------- CSV READINFG ----------------------------
try:

    data_frame = pandas.read_csv("Udemy/31-day/data/words_to_learn.csv")
    data = data_frame.to_dict(orient="records")

except FileNotFoundError:

    data_frame = pandas.read_csv("Udemy/31-day/data/french_words.csv")
    data = data_frame.to_dict(orient="records")

finally:

    print(data[0]['French']) # Format to acces french words

    print(data[0]['English'])

    print(len(data)) # 101
 
# ---------------------------- Change Word ----------------------------

def change_word():
    """Changes the word of the canvas for another random one."""

    global language_title, current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    # Changing title to 'French' and a random new french word
    language_title = "French"
    canvas.itemconfig(title_text, text = language_title, fill="black")
    french_word = current_card["French"]
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=canvas_img_front)

    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ----------------------------

def flip_card():
    global language_title, current_card

    language_title = "English"
    # canvas.create_image(400, 263, image=canvas_img_back)
    canvas.itemconfig(title_text, text =language_title, fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=canvas_img_back)

# ---------------------------- SAVE ----------------------------

def save(): 
    """Changes the word of the canvas for another random one."""

    global language_title, current_card, flip_timer

    index_current_card = data.index(current_card)

    print(current_card)
    print(index_current_card)

    del data[index_current_card]

    words_to_learn = pandas.DataFrame(data)

    words_to_learn = words_to_learn.to_csv("Udemy/31-day/data/words_to_learn.csv", index=False)

    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    # Changing title to 'French' and a random new french word
    language_title = "French"
    canvas.itemconfig(title_text, text = language_title, fill="black")
    french_word = current_card["French"]
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=canvas_img_front)

    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- UI INTERFACE ----------------------------

# Root
window = Tk()
window.title("Flash Card Proyect")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas_img_front = PhotoImage(file="Udemy/31-day/images/card_front.png")

canvas_img_back = PhotoImage(file="Udemy/31-day/images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=canvas_img_front)
canvas.grid(column=0, row=0, columnspan=2)

# Canvas text
title_text = canvas.create_text(400, 150, text=language_title, fill="black", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))

# Buttons
cross_image = PhotoImage(file="Udemy/31-day/images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=change_word)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="Udemy/31-day/images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=save)
tick_button.grid(row=1, column=1)

change_word()

window.mainloop()
