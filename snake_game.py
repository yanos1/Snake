from typing import Optional
from game_display import GameDisplay, CELL_SIZE, NUM_OF_WALLS
from game_utils import get_random_apple_data, UP,get_random_wall_data
from snake import Snake
from apple import Apple
import math
from wall import Wall

class SnakeGame:

    def __init__(self,width = 40,height = 30, max_apples = 3, debug = False,
                 max_walls = NUM_OF_WALLS, rounds = -1 ) -> None:
        self.width = width
        self.height = height
        self.max_apples = max_apples
        self.debug = debug
        self.max_walls = max_walls
        self.rounds = rounds
        self.snake = None
        self.apple_count = 0
        self.apples = []
        self.apple_locations = []
        self.walls = []
        self.wall_count = 0
        self.__key_clicked = None
        self._is_over = False
        self.score = 0


    def start_game(self):
        self.snake = Snake("black", 3, UP, (self.width//2,self.height//2))
        self.apples.append(Apple("green", CELL_SIZE,get_random_apple_data()))
        self.apple_locations.append(self.apples[0].location)
        self.apple_count += 1
        self.wall = Wall(3, "blue")
        self.walls.append(self.wall)

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def single_round(self, gd:GameDisplay):
        if self.__key_clicked:
            self.snake.change_direction(self.__key_clicked)
        if self.snake.growth > 0:
            self.snake.grow_snake()
        self.check_walls()
        if self.wall_count < self.max_walls:
            self.add_wall()
        if self.snake.location in self.apple_locations:#if snake eat apple#change score and remove apple
            self.eat_apple(gd)
        if self.snake.growth == 0:
            self.snake.move_snake()
        if self.rounds % 2 == 0:
            self.move_walls()
        if self.apple_count < self.max_apples:
            self.add_apple()
        if not self.debug:
            self.draw_snake(gd)
        self.draw_apples(gd)
        self.draw_wall(gd)
        self.rounds += 1

    def eat_apple(self, gd:GameDisplay):
        self.score += math.floor(math.sqrt(len(self.snake.locations)))
        gd.show_score(self.score)
        self.snake.growth += 3
        for apple in self.apples:
            if apple.location == self.snake.location:
                self.apples.remove(apple)
                self.apple_locations.remove(apple.location)
                break
        self.apple_count -= 1

    def add_apple(self):
        loc = get_random_apple_data()
        if loc not in self.snake.locations and loc not in self.apple_locations \
                and loc not in [wall.locations for wall in self.walls]:
            new_apple = Apple("green", CELL_SIZE, loc)
            self.apples.append(new_apple)
            self.apple_locations.append(new_apple.location)
            self.apple_count += 1

    def draw_snake(self, gd: GameDisplay) -> None:
        # draw snake
        for location in self.snake.locations:
            gd.draw_cell(location[0], location[1], self.snake.color)

    def draw_apples(self,gd: GameDisplay):
        # draw apple
      for apple in self.apples:
            gd.draw_cell(apple.location[0], apple.location[1],apple.color)

    def draw_wall(self, gd: GameDisplay):
        for wall in self.walls:
            for loc in wall.locations:
                gd.draw_cell(loc[0], loc[1], wall.color)

    def end_round(self) -> None:
        if self.snake.self_collision():
            self._is_over = True
        for wall in self.walls:
            if self.snake.location in wall.locations:
                self._is_over = True
                self.snake.locations = []

    def is_over(self) -> bool:
        return self._is_over

    def add_wall(self):
        new_wall = Wall(3, "blue")
        for loc in new_wall.locations:
            if loc in self.snake.locations or loc in self.apple_locations \
                or loc in [wall.locations for wall in self.walls]:
                return
        self.walls.append(new_wall)
        self.wall_count += 1

    def check_walls(self):
        for wall in self.walls:
            if len(wall.locations) == 0:
                self.walls.remove(wall)
                self.wall_count -= 1

    def move_walls(self):
        for wall in self.walls:
            wall.move_wall()