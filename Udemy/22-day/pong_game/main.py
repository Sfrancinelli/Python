from turtle import Turtle, Screen
import paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = paddle.Paddle(-350, 0)
r_paddle = paddle.Paddle(350, 0)

ball = Ball()

score = Scoreboard()

screen.listen()

screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)

screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    l_paddle.singleplayer()

    # Detext collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.xcor() > 385 or ball.xcor() < -385:
        score.game_over()
        game_is_on = False
    

    # Detect collision with r_paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 325:
        ball.bounce_x()

    # Detect collision with l_paddle
    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -325:
        ball.bounce_x()


screen.exitonclick()
