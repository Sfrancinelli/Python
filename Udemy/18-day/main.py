from turtle import Turtle, Screen, color, colormode
from random import randint

tim = Turtle()
colormode(255)

tim.shape("turtle")
tim.color("coral")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.fd(100)
        tim.left(angle)

for shape_side_n in range(3,11): # From a triangle (3 sides) to a decagon (10 sides)!
    tim.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))
    draw_shape(shape_side_n)


# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(4):
#     tim.fd(100)
#     tim.left(90)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(5):
#     tim.fd(100)
#     tim.left(72)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(6):
#     tim.fd(100)
#     tim.left(60)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(7):
#     tim.fd(100)
#     tim.left(360/7)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(8):
#     tim.fd(100)
#     tim.left(360/8)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(9):
#     tim.fd(100)
#     tim.left(360/9)

# tim.color(randint(0, 255),
#           randint(0, 255),
#           randint(0, 255))
# for i in range(10):
#     tim.fd(100)
#     tim.left(36)















screen = Screen()
screen.exitonclick()