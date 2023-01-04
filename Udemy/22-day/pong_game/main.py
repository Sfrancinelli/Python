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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # if ball.ycor() > 0:
    #     if l_paddle.ycor() < 230:
    #         l_paddle.up()
    # elif ball.ycor() < 0:
    #     if l_paddle.ycor() > -230:
    #         l_paddle.down()


    # IA OP, Never misses

    if l_paddle.ycor() < ball.ycor():
        l_paddle.up()
    elif l_paddle.ycor() > ball.ycor():
        l_paddle.down()


    # Detext collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    
    # Detect R paddle misses
    if ball.xcor() > 385:
        ball.reset_position()
        score.r_point()
    
    # Detect L paddle misses
    if ball.xcor() < -385:
        ball.reset_position()
        score.l_point()
    
    # Detect collision with r_paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() >= 325:
        ball.bounce_x()
        # ball.speeeeeeeeeeed()

    # Detect collision with l_paddle
    if ball.distance(l_paddle) <= 50 and ball.xcor() <= -325:
        ball.bounce_x()
        # ball.speeeeeeeeeeed()


screen.exitonclick()
