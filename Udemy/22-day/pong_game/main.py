from turtle import Turtle, Screen
import paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong Game")
# screen.tracer(0)

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
    # screen.update()
    ball.move()


screen.exitonclick()
