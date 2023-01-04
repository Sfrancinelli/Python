from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(-250, 275)
        self.level = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 275)
        self.write(self.level, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        
