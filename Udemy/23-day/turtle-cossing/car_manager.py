from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.goto(300, randint(-250, 250))
        self.starting_speed = STARTING_MOVE_DISTANCE
        self.speeding = MOVE_INCREMENT

    
