import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

GAME_SPEED_INCREMENTS = 0.95


class TurtleCrossingGame:
    def __init__(self):
        self.game_speed = 0.1
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.player = Player()
        self.screen.onkeypress(self.player.move, "Up")
        self.screen.listen()
        self.score_board = Scoreboard(self.screen)
        self.car_manager = CarManager()

    def play(self):
        game_is_on = True
        add_car_counter = 0
        while game_is_on:
            game_is_on = self.is_game_on()
            add_car_counter += 1
            time.sleep(self.game_speed)
            self.car_manager.move_cars()
            if self.player.reached_other_side():
                self.level_up()
            if add_car_counter == 8:
                self.car_manager.add_cars_to_cars_list()
                add_car_counter = 0
            self.screen.update()
        self.score_board.write_game_over()
        self.screen.exitonclick()

    def is_game_on(self):
        return not self.car_manager.did_collision_happen(self.player.pos())

    def level_up(self):
        self.game_speed *= 0.99
        self.player.reset_turtle()
        self.score_board.new_level()
        self.score_board.clear_and_write_new_level()
        self.car_manager.speed_up_cars()
