from turtle import Screen, Turtle, time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakes = []

x = 0

for _ in range(3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(x, 0)
    x -= 20
    snakes.append(snake)

screen.update()

game_is_on = True
while game_is_on:        
    screen.update()
    time.sleep(.1)
    for snake in snakes:
        snake.fd(20)
        

screen.exitonclick()