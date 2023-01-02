from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
colormode(255)

tim.shape("turtle")
tim.speed("fastest")


def spirograph(n_circles, radius_circle):
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    tim.circle(radius_circle)
    angle = 360 / n_circles
    tim.right(angle)


num_circles = int(input("How many circles do you want?: "))

for _ in range (num_circles):
    spirograph(num_circles, 200)

screen = Screen()
screen.exitonclick()