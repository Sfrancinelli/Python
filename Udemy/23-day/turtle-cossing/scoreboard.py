from turtle import Turtle, Screen

FONT = ("Courier", 20, "normal")

GAME_OVER_FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(-220, 275)
        self.level = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
        
