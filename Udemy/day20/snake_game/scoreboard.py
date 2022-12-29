from turtle import Turtle, Screen

ALIGNMENT = "center"

FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.show_score()
        

    def add_score(self):
        self.score += 1
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
