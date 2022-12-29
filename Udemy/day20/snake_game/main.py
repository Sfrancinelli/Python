from turtle import Screen, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#D9D6CB")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:        
    screen.update()
    time.sleep(0.05)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 305 or snake.head.ycor() < -305:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]: # Slicing
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 8:
            game_is_on = False
            scoreboard.game_over()
      

screen.exitonclick()