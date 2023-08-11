import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkeypress(player.move_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # TODO Detect collision between car and turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # TODO Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.move_speed *= 0.9

screen.exitonclick()
