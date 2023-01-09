import argparse

from snake_game import SnakeGame
from game_display import GameDisplay


def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame(args.width, args.height, args.apples, args.debug,
                     args.walls, args.rounds)
    game.start_game()
    gd.show_score(0)

    # DRAW initial BOARD
    game.draw_snake(gd)
    game.draw_apples(gd)
    game.draw_walls(gd)
    # END OF ROUND 0
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # Draw and move objects
        game.single_round(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")
