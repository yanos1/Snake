from game_utils import UP, DOWN, LEFT,RIGHT
from typing import *


class Snake:
    def __init__(self,color, size, direction, location) -> None:
        self.color = color
        self.size = size
        self.direction = direction
        self.location = location
        self.locations = self.build_snake(location)

    def build_snake(self,location, direction=UP, snake_length=3):
        if direction == UP:
            return [(location[0], location[1] - i) for i in range(snake_length)]
        elif direction == DOWN:
            return [(location[0], location[1] + i) for i in range(snake_length)]
        elif direction == RIGHT:
            return [(location[0] - i, location[1]) for i in range(snake_length)]
        elif direction == LEFT:
            return [(location[0] + i, location[1]) for i in range(snake_length)]

    def move_snake(self):
        if self.direction == UP:
            self.location = (self.location[0],self.location[1]+1)
        elif self.direction == DOWN:
            self.location = (self.location[0],self.location[1]-1)
        elif self.direction == RIGHT:
            self.location = (self.location[0]+1,self.location[1])
        else:
            self.location = (self.location[0]-1,self.location[1])
        # actual movement
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

    def self_collision(self):
        if self.locations.count(self.location) == 2:
            return True
        return False


















