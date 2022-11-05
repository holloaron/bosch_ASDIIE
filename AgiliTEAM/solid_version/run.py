import curses
from argparse import ArgumentParser

from bosch_ASDIIE.AgiliTEAM.solid_version.core.game import Game
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_listener import KeyListener
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman_game_state import PacmanGameState
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman import Pacman
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pellets import Pellets
from bosch_ASDIIE.AgiliTEAM.solid_version.core.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.visualizer import Visualizer
from bosch_ASDIIE.AgiliTEAM.solid_version.gui.console_canvas import ConsoleCanvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.map import MapSize
from bosch_ASDIIE.AgiliTEAM.solid_version.core.screen import Screen
from bosch_ASDIIE.AgiliTEAM.solid_version.core.score_counter import ScoreCounter
from bosch_ASDIIE.AgiliTEAM.solid_version.core.defeat_checker import DefeatChecker

# Defaults
WIDTH = 10
HEIGHT = 10
GUI = 'console'
DIFFICULTY = 0.5
PELLETS = 10
GHOSTS = 4
BASE_SCORE = 10


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--gui", type=str, default=GUI)
    arg_parser.add_argument("--map_width", type=int, default=WIDTH)
    arg_parser.add_argument("--map_height", type=int, default=HEIGHT)
    arg_parser.add_argument("--difficulty", type=float, default=DIFFICULTY)
    arg_parser.add_argument("--num_pellets", type=int, default=PELLETS)
    arg_parser.add_argument("--num_ghosts", type=int, default=GHOSTS)
    arg_parser.add_argument("--base_score", type=int, default=BASE_SCORE)
    args = arg_parser.parse_args()

    screen = Screen()
    curses.cbreak()

    key_listener = KeyListener()
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