from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
colormode(255)

tim.shape("turtle")
tim.color("coral")


tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(4):
    tim.fd(100)
    tim.left(90)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(5):
    tim.fd(100)
    tim.left(72)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(6):
    tim.fd(100)
    tim.left(60)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(7):
    tim.fd(100)
    tim.left(360/7)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(8):
    tim.fd(100)
    tim.left(360/8)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(9):
    tim.fd(100)
    tim.left(360/9)

tim.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
for i in range(10):
    tim.fd(100)
    tim.left(36)















screen = Screen()
screen.exitonclick()