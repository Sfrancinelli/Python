from turtle import Turtle, Screen
import paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong Game")
screen.tracer(0)

paddle_2 = paddle.Paddle(-350, 0)
paddle = paddle.Paddle(350, 0)

screen.listen()

screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

screen.onkey(key="w", fun=paddle_2.up)
screen.onkey(key="s", fun=paddle_2.down)

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
