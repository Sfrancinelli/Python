from turtle import Turtle, Screen
import paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = paddle.Paddle(-350, 0)
r_paddle = paddle.Paddle(350, 0)

ball = Ball()

screen.listen()

screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.xcor() > 385 or ball.xcor() < -385:
        game_is_on = False

screen.exitonclick()
