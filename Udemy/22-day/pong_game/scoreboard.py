from turtle import Turtle, Screen

FONT = ('Courier', 50, 'normal')
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 225)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 225)
        self.write(self.r_score, align="center", font=FONT)


    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

                
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()