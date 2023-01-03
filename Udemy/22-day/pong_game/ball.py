from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1,1)
        self.color("white")
        self.pu()
        self.goto(0,0)
        self.speed("fast")
        self.x = self.xcor()
        self.y = self.ycor()
        self.heading = self.heading()

    def move(self):
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)  
            if self.ycor() >= 290 or self.ycor() <= -290:
                self.right(50)      