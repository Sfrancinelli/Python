# Speed from 1 (slower) to 10 (fastest) (0 is the fastest, with no animation)
from turtle import Turtle, Screen
from random import randint


screen = Screen()

screen.setup(width = 800, height = 500)

# Instance of turtles
tim = Turtle()
tom = Turtle()
tam = Turtle()
tem = Turtle()
tum = Turtle()

# Color of turtles
tim.color("red")
tom.color("green")
tam.color("blue")
tem.color("grey")
tum.color("black")

turtles = []

# Appending turtles into list for better management
turtles.append(tim)
turtles.append(tom)
turtles.append(tam)
turtles.append(tem)
turtles.append(tum)

y = -100

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def race():
    racing = True
    while racing:
        for turtle in turtles:
            if turtle.xcor() < 380:
                turtle.fd(randint(5, 20))
                racing = True
            else:
                racing = False

            if turtle.xcor() >= 380:
                return turtle.color()

for turtle in turtles:
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(-390, y)
    y += 50

winner = race()

if bet.lower() == winner[0].lower():
    print("You win, congratulations!")
else:
    print("You lose!")

screen.exitonclick()