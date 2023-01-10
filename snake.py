from game_utils import UP, DOWN, LEFT, RIGHT
from typing import Any, List


class Snake:
    def __init__(self, color, size, direction, location) -> None:
        self.color = color
        self.size = size
        self.direction = direction
        self.location = location
        self.locations = self.build_snake(location)
        self.growth = 0

    def build_snake(self, location):
        return [(location[0], location[1] - i) for i in range(self.size)]

    def add_head(self):
        if self.direction == UP:
            self.location = (self.location[0], self.location[1] + 1)
        elif self.direction == DOWN:
            self.location = (self.location[0], self.location[1] - 1)
        elif self.direction == RIGHT:
            self.location = (self.location[0] + 1, self.location[1])
        else:
            self.location = (self.location[0] - 1, self.location[1])
            # actual movement
        self.locations.insert(0, self.location)

    def move_snake(self):
        self.add_head()
        self.locations.pop()

    def possible_moves(self) -> List:
        if self.direction == UP or self.direction == DOWN:
            pos_moves = [RIGHT, LEFT]
        else: # Right, or left
            pos_moves = [UP, DOWN]
        return pos_moves

    def change_direction(self, move_key):
        if move_key in self.possible_moves():
            self.direction = move_key
            return True
        return

    def self_collision(self):
        if self.locations.count(self.location) == 2:
            return True
        return False

    def grow_snake(self):
        self.add_head()
        self.growth -= 1

















