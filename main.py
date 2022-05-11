import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("silver")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

for i in range(20):
    car_manager.create_top_cars()
    car_manager.create_bottom_cars()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # car_manager.move_cars()
    car_manager.move_cars()

    # Cars enter and exit the screen
    car_manager.check_cars_on_screen()

    # Detect collision with the car
    for car in car_manager.top_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    for car in car_manager.bottom_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()

