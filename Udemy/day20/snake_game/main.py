from turtle import Screen, time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

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
      

screen.exitonclick()