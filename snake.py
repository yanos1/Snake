from snake_game import SnakeGame as sg
from game_utils import UP, DOWN, LEFT,RIGHT
from game_display import GameDisplay as gd
from typing import *

class Snake:
    def __init__(self,color, size, direction, location) -> None:
        self.color = color
        self.size = size
        self.direction = direction
        self.location = location
        self.pos_moves = []

    def possible_moves(self) -> List:
        if self.direction == UP or self.direction == DOWN:
            self.pos_moves = [RIGHT,LEFT]
        elif self.direction == RIGHT or self.direction == LEFT:
            self.pos_moves  = [UP,DOWN]
        return self.pos_moves

    def change_direction(self, move_key):
        #i check direction
        # i check move_key
        # if they are valid i change
        # return True if i made it, and call "change location" fucntion,
        # else otherwise return False
        if move_key in self.possible_moves():
            self.direction = move_key
            self.move(move_key)













