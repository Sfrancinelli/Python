from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Creates a playing turtle ready to cross the street"""

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.goto(STARTING_POSITION)
        self.speed("fast")

    def up(self):
        """Moves the turtle up 10px at a time"""

        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves the turtle down 10px at a time"""

        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
