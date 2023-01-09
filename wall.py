from game_utils import get_random_wall_data, WIDTH, HEIGHT, UP, DOWN, RIGHT\
    , LEFT
from game_display import argparse


class Wall:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        x, y, direction = get_random_wall_data()
        self.location = (x, y)
        self.direction = direction
        self.head = self.set_head()
        self.locations = self.get_location(x, y, direction)

    def get_head(self):
        return self.head

    def set_head(self):
        if self.direction == UP:
            self.head = (self.location[0], self.location[1] + 1)
        elif self.direction == DOWN:
            self.head = (self.location[0], self.location[1] - 1)

        elif self.direction == RIGHT:
            self.head = (self.location[0] + 1, self.location[1])

        elif self.direction == LEFT:
            self.head = (self.location[0] - 1, self.location[1])
        return self.head

    def get_location(self, x, y, direction):
        if direction in ["Up", "Down"]:
            return [(x, y - self.size//2 + i) for i in range(self.size)
                 if y - self.size//2 + i < HEIGHT and y- self.size//2 + i >= 0]

        if direction in ["Right", "Left"]:
            return [(x - self.size//2 + i, y) for i in range(self.size)
                    if x - self.size//2 + i >= 0 and x- self.size//2 + i < WIDTH]

    def move_wall(self):
        if self.direction == UP:
            self.location = (self.location[0], self.location[1]+1)
            self.head = (self.location[0], self.location[1]+1)
        elif self.direction == DOWN:
            self.location = (self.location[0], self.location[1] - 1)
            self.head = (self.location[0], self.location[1] - 1)

        elif self.direction == RIGHT:
            self.location = (self.location[0] + 1, self.location[1])
            self.head = (self.location[0]+1, self.location[1])

        elif self.direction == LEFT:
            self.location = (self.location[0] - 1, self.location[1])
            self.head = (self.location[0]-1, self.location[1])

        self.locations = self.get_location(self.location[0], self.location[1],
                                           self.direction)

