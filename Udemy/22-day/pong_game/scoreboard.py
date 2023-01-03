from turtle import Turtle, Screen

ALIGNMENT = "center"

FONT = ('Courier', 50, 'normal')

GAME_OVER_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 225)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 225)
        self.write(self.r_score, align="center", font=FONT)
        
        

    def add_score(self):
        self.score += 1
        self.show_score()

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)