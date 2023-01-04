from turtle import Turtle, Screen

ALIGNMENT = "center"

FONT = ('Courier', 16, 'normal')

GAME_OVER_FONT = ('Courier', 24, 'normal')

file = open("Udemy/20-day/snake_game/high_score.txt", mode="r")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.ht()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.high_score = file.read()
        self.show_score()
        

    def add_score(self):
        self.score += 1
        self.show_score()

    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)


    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        with open("Udemy/20-day/snake_game/high_score.txt", mode="r") as file:
            high_score = file.read()
            if self.score > int(high_score):
                self.high_score = self.score
                with open("Udemy/20-day/snake_game/high_score.txt", mode="w") as file:
                    file.write(str(self.high_score))
        self.score = 0
        self.show_score()

file.close()