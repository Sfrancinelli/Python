from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", highlightthickness=0, bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.q_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=("Arial", 16, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        self.true_img = PhotoImage(file="Udemy/34-day/images/true.png")
        self.false_img = PhotoImage(file="Udemy/34-day/images/false.png")

        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.q_text, text=question_text)

