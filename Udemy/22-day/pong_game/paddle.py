from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1,outline=1)
        self.pu()
        self.goto(x_cor, y_cor)
        self.speed("fastest")
        self.game_is_on = True

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)




