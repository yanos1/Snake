from typing import Optional
from game_display import GameDisplay
from apple import Apple
from game_utils import get_random_apple_data

class SnakeGame:

    def __init__(self,) -> None:
        self.apple_count = 0
        self.max_apples = 3 #agrssss
        self.apple_locations = []

        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def get_key_clicked(self): #mine
        return self.__key_clicked()

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
        elif (self.__key_clicked == 'Right') and (self.__x < 40):
            self.__x += 1

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "black")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False

