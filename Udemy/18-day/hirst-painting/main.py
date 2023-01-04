import colorgram
from turtle import Turtle, Screen, color, colormode
from random import randint, choice

# colors = colorgram.extract("C:/Users/Esteban/Desktop/SF/Curso-Udemy/Udemy/day18/hirst-painting/imagen.jpg", 30)

# first_color = colors[0]

# rgb = first_color.rgb

# print(rgb)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g , b)
#     rgb_colors.append(new_color)

color_list = [(242, 230, 68), (184, 18, 42), (253, 235, 240), (219, 238, 244), (188, 72, 35), (16, 139, 83), (113, 180, 207), (191, 179, 21), (23, 121, 168), (24, 38, 74), (219, 60, 97), (241, 232, 2), (212, 161, 92), (75, 174, 96), (180, 44, 62), (37, 45, 112), (15, 165, 
212), (220, 130, 157), (216, 71, 51), (125, 184, 123), (6, 59, 38), (166, 27, 24), (9, 94, 54), (238, 157, 178), (147, 208, 221), (5, 85, 111), (160, 212, 182), (237, 170, 163)]

colormode(255)

tim = Turtle()

tim.shape("turtle")
tim.speed("fastest")

current_y = -225


def dot_line():

    global current_y

    tim.penup()
    tim.hideturtle()
    tim.goto(-225, current_y)

    for _ in range(10):

        tim.color(choice(color_list))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.fd(50)
        tim.pendown()

    current_y += 50
    tim.penup()
    tim.goto(-200, current_y)


for _ in range(10):
    dot_line()

screen = Screen()
screen = screen.exitonclick()
