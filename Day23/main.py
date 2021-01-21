import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(player.move_forward, 'Up')
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_car()
    car_manager.update_list()
    if car_manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()
    if player.reached_top_edge():
        screen.tracer(0)
        car_manager.increment_speed_of_cars()
        scoreboard.increase_level()


    screen.update()
