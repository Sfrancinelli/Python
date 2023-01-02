from turtle import Turtle, Screen, clearscreen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.back(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key = "w", fun = move_forwards)
screen.onkeypress(key = "s", fun = move_backwards)
screen.onkeypress(key = "a", fun = turn_left)
screen.onkeypress(key = "d", fun = turn_right)

screen.onkey(key = "c", fun = clear)

screen.exitonclick()