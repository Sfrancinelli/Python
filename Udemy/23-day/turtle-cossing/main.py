import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint, choice

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=player.up)
screen.onkeypress(key="Down", fun=player.down)

cars = []

for _ in range(randint(0,20)):
    car = CarManager()
    cars.append(car)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    choice(cars).move()

    if player.ycor() > 275:
        scoreboard.level_up()
        player.next_level()
        for car in cars:
            car.level_up()
            car.reset_position()


screen.exitonclick()
