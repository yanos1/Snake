from snake_game import SnakeGame as sg
from game_utils import UP, DOWN, LEFT,RIGHT
from game_display import GameDisplay as gd
from typing import *
from game_display import parse_args
#במחלקה זו ניצור אובייקט מסוג נחש.
# לנחש יש כיוון, מיקום,צבע,
# נממש פה תזוזה של הנחש,
class Snake:
    def __init__(self,color, size, direction, location) -> None:
        self.color = color
        self.size = size
        self.direction = direction
        self.location = location
        self.locations = [(5,5),(5,4),(5,3),(5,2),(5,1),(5,0)]

    def move_snake(self):
        if self.direction == UP:
            self.location = (self.location[0],self.location[1]+1)
        elif self.direction == DOWN:
            self.location = (self.location[0],self.location[1]-1)
        elif self.direction == RIGHT:
            self.location = (self.location[0]+1,self.location[1])
        else:
            self.location = (self.location[0]-1,self.location[1])
        self.locations.insert(0,self.location)
        self.locations.pop()

    def possible_moves(self) -> List:
        if self.direction == UP or self.direction == DOWN:
            self.pos_moves = [RIGHT,LEFT]
        elif self.direction == RIGHT or self.direction == LEFT:
            self.pos_moves  = [UP,DOWN]
        return self.pos_moves


    def change_direction(self, move_key):
        if move_key in self.possible_moves():
            self.direction = move_key
            return True
        return

    def collision(self):
        if self.locations.count(self.location) == 2:
            return True
        return False


















