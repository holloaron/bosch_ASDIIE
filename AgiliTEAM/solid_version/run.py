import curses
from argparse import ArgumentParser

from bosch_ASDIIE.solid_version.core.game import Game
from bosch_ASDIIE.solid_version.core.key_listener import KeyboardListener
from bosch_ASDIIE.solid_version.core.snake_game_state import SnakeGameState
from bosch_ASDIIE.solid_version.core.snake import Snake
from bosch_ASDIIE.solid_version.core.visualizer import Visualizer
from bosch_ASDIIE.solid_version.gui.console_canvas import ConsoleCanvas
from bosch_ASDIIE.solid_version.core.map import MapSize
from bosch_ASDIIE.solid_version.core.screen import Screen

WIDTH = 20
HEIGHT = 20


def main():
    # arg parser
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--gui", type=str, default="console")
    args = arg_parser.parse_args()

    # using curses lib for proper keyboard-canvas interaction through SSH
    screen = Screen()
    curses.cbreak()

    key_listener = KeyboardListener()
    key_listener.start(screen)

    snake = Snake(map_size=MapSize(HEIGHT, WIDTH))
    visualizer = Visualizer([snake], ConsoleCanvas(MapSize(HEIGHT, WIDTH), screen))
    start_game_state = SnakeGameState([snake])
    game = Game(key_listener, start_game_state, visualizer)
    game.run()

    # stop the screen
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

if __name__ == "__main__":
    main()