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
car = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player.up)
screen.onkeypress(key="Down", fun=player.down)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    if player.ycor() > 275:
        scoreboard.level_up()
        player.next_level()
        car.level_up()


    # for car in car.all_cars:
    #     if player.distance(car) < 20:
    #         game_is_on = False
    #         scoreboard.game_over()




screen.exitonclick()
