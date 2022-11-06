import curses
from argparse import ArgumentParser

from Objects.core.game import Game
from Objects.core.get_action import KeyEvent
from Objects.core.map import MapSize
from Objects.core.screen import Screen
from Objects.core.visualizer import Visualizer
#TODO
from Objects.core.pacman_game_state import
from Objects.core.pacman import
from Objects.gui.console_canvas import


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