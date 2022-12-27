from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
colormode(255)

tim.shape("turtle")
tim.color("coral")

def random_walk():
    path = randint(0, 2)
    # thickness = randint(0, 4)
    # tim.width(thickness)
    tim.width(7)
    if path == 0:
        tim.left(90)
    elif path == 1:
        tim.right(90)
    elif path == 3:
        tim.fd(20)
    
for _ in range(200):
    tim.fd(20)
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    random_walk()

screen = Screen()
screen.exitonclick()
    