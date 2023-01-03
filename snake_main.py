import argparse
from game_utils import UP, DOWN,LEFT,RIGHT
from snake_game import SnakeGame
from game_display import GameDisplay
from snake import Snake

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame()
    snake = Snake("black",3,UP,(5,5))
    gd.show_score(0)

    # DRAW BOARD
    game.draw_board(gd)
    # END OF ROUND 0
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        if key_clicked:
            snake.change_direction(key_clicked)
            print(snake.direction)
        snake.move_snake()
        # UPDATE OBJECTS
        game.update_objects()
        # DRAW BOARD
        for location in snake.locations:
            gd.draw_cell(location[0],location[1],snake.color)
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")