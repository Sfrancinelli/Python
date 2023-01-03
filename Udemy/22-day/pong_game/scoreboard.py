from turtle import Turtle, Screen

ALIGNMENT = "center"

FONT = ('Courier', 16, 'normal')

GAME_OVER_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        # self.show_score()
        

    def add_score(self):
        self.score += 1
        self.show_score()

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)