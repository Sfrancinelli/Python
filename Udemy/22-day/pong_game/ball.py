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

    def move(self):
            if self.xcor() < 335 or self.xcor > -335:
                self.fd(10)
            if self.xcor() >= 335 or self.xcor() <= -335:
                if self.heading() == 45:
                    self.setheading(135)
                    self.fd(10)
                elif self.heading() == 135:
                    self.setheading(225)
                    self.fd(10)
                elif self.heading() == 225:
                    self.setheading(315)
                    self.fd(10)
                elif self.heading() == 315:
                    self.setheading(45)
                    self.fd(10)                