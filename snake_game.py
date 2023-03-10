from typing import Optional
from game_display import GameDisplay, CELL_SIZE, NUM_OF_WALLS
from game_utils import get_random_apple_data, UP, WIDTH, HEIGHT
from snake import Snake
from apple import Apple
import math
from wall import Wall


class SnakeGame:
    def __init__(self, width=40, height=30, max_apples=10, debug=False,
                 max_walls=3, rounds=-1) -> None:
        self.width = width
        self.height = height
        self.max_apples = max_apples
        self.debug = debug
        self.max_walls = max_walls
        self.rounds = 0
        self.max_round = rounds
        self.snake = None
        self.apple_count = 0
        self.apples = []
        self.apple_locations = []
        self.walls = []
        self.wall_count = 0
        self.__key_clicked = None
        self._is_over = False
        self.wall = None
        self.score = 0

    def start_game(self, gd: GameDisplay):
        if self.debug:
            self.snake = Snake("black", 0, UP,
                               (self.width // 2, self.height // 2))
        else:
            self.snake = Snake("black", 3, UP,
                               (self.width // 2, self.height // 2))
        if self.max_walls > 0:
            self.wall = Wall(3, "blue")
            self.walls.append(self.wall)
            self.wall_count += 1
        if self.max_apples > 0:
            self.apples.append(
                Apple("green", CELL_SIZE, get_random_apple_data()))
            self.apple_locations.append(self.apples[0].location)
            self.apple_count += 1
        self.draw_snake(gd)
        self.draw_walls(gd)
        self.draw_apples(gd)

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def single_round(self, gd: GameDisplay):
        if self.__key_clicked:
            self.snake.change_direction(self.__key_clicked)
        self.check_walls()
        if self.rounds > 0:
            if self.snake.growth > 0:
                self.snake.grow_snake()
            if self.snake.growth == 0:
                self.snake.move_snake()
            if self.rounds % 2 == 0:
                self.move_walls()
            self.wall_snake(gd)
            collision = self.wall_apple()
            for i in range(collision):
                self.add_apple()
            if self.snake.location in self.apple_locations:
                self.eat_apple(gd)
            if self.wall_count < self.max_walls:
                self.add_wall()
            if self.apple_count < self.max_apples:
                self.add_apple()
            if not self.debug:
                self.draw_snake(gd)
            self.end_round()
            self.draw_walls(gd)
            self.draw_apples(gd)


    def eat_apple(self, gd: GameDisplay):
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

    def draw_apples(self, gd: GameDisplay):
        # draw apple
        for apple in self.apples:
            gd.draw_cell(apple.location[0], apple.location[1], apple.color)

    def draw_walls(self, gd: GameDisplay):
        for wall in self.walls:
            for loc in wall.locations:
                gd.draw_cell(loc[0], loc[1], wall.color)

    def end_round(self) -> None:
        if self.max_round == self.rounds:
            self._is_over = True
        if self.snake.self_collision():
            self._is_over = True
        if self.snake.location[0] == WIDTH or self.snake.location[1] == HEIGHT:
            self.snake.locations.remove(self.snake.location)
            self._is_over = True
        for wall in self.walls:
            if self.snake.location in wall.locations:
                self._is_over = True
                self.snake.locations = []
        if len(self.snake.locations) == 1:
            self._is_over = True
        self.rounds += 1

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

    def wall_apple(self):
        check = 0
        for apple in self.apples:
            for wall in self.walls:
                if apple.location == wall.get_head():
                    self.apple_locations.remove(wall.get_head())
                    self.apples.remove(apple)
                    check += 1
        return check


    def wall_snake(self, gd: GameDisplay):
        for wall in self.walls:
            if wall.get_head() in self.snake.locations[1:]:
                gd.draw_cell(wall.get_head()[0], wall.get_head()[1],
                             wall.color)
                idx = self.snake.locations.index(wall.get_head())
                self.snake.locations = self.snake.locations[:idx]
