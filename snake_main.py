import argparse
from game_utils import UP, DOWN,LEFT,RIGHT, get_random_apple_data
from snake_game import SnakeGame
from game_display import GameDisplay, CELL_SIZE
from snake import Snake
from apple import Apple



def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:

    # INIT OBJECTS
    game = SnakeGame()
    snake = Snake("black",3,UP,(5,5))
    apple = Apple("green",CELL_SIZE,get_random_apple_data())
    game.apple_locations.append(apple.location)
    game.apple_count+=1
    gd.show_score(0)

    # DRAW BOARD
    for location in snake.locations:
        gd.draw_cell(location[0], location[1], snake.color)
    gd.draw_cell(apple.location[0],apple.location[1],apple.color)
    # END OF ROUND 0
    while not game.is_over():
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        if key_clicked:
            snake.change_direction(key_clicked)
        snake.move_snake()
        # UPDATE OBJECTS
        # DRAW BOARD
        for location in snake.locations:
            gd.draw_cell(location[0],location[1],snake.color)
        if game.apple_count < game.max_apples:
            loc = get_random_apple_data()
            if loc not in snake.locations and loc not in game.apple_locations:
                new_apple = Apple("green",CELL_SIZE,loc)
                game.apple_locations.append(new_apple.location)
                game.apple_count+=1

        for cell in game.apple_locations:
            gd.draw_cell(cell[0],cell[1],apple.color)










        if snake.collision():
            break
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()

if __name__ == "__main__":
    print("You should run:\n"
          "> python game_display.py")