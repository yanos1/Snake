from typing import Optional
from game_display import GameDisplay, CELL_SIZE
from game_utils import get_random_apple_data, UP,DOWN,LEFT,RIGHT
from snake import Snake
from apple import Apple


class SnakeGame:

    def __init__(self,width,height, max_apples) -> None:
        self.width = width
        self.height = height
        self.apple_count = 0
        self.max_apples = max_apples
        self.apples = []
        self.snake = None
        self.__key_clicked = None
        self._is_over = False

    def start_game(self):
        self.snake = Snake("black", 3, UP, (self.width//2,self.height//2))
        self.apples.append(Apple("green", CELL_SIZE, get_random_apple_data()))
        self.apple_count += 1

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def single_round(self, gd:GameDisplay):
        if self.__key_clicked:
            self.snake.change_direction(self.__key_clicked)
        self.snake.move_snake()
        if self.apple_count < self.max_apples:
            loc = get_random_apple_data()
            if loc not in self.snake.locations and loc not in \
                    [apple.location for apple in self.apples]:
                self.apples.append(Apple("green", CELL_SIZE, loc))
                self.apple_count += 1
        self.draw_snake(gd)
        self.draw_apple(gd)


    def draw_snake(self, gd: GameDisplay) -> None:
        # draw snake
        for location in self.snake.locations:
            gd.draw_cell(location[0], location[1], self.snake.color)

    def draw_apple(self,gd: GameDisplay):
        # draw apple
        print(len(self.apples))
        for apple in self.apples:
            gd.draw_cell(apple.location[0], apple.location[1],
                         apple.color)

    def end_round(self) -> None:
        collision = self.snake.self_collision()
        if collision:
            self._is_over = True

    def is_over(self) -> bool:
        return self._is_over




