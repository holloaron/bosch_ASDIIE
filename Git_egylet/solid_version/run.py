import curses
from argparse import ArgumentParser

from bosch_ASDIIE.Git_egylet.solid_version.core.game import Game
from bosch_ASDIIE.Git_egylet.solid_version.core.key_listener import KeyListener
from bosch_ASDIIE.Git_egylet.solid_version.core.pacman_game_state import PacmanGameState
from bosch_ASDIIE.Git_egylet.solid_version.core.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.core.pellets import Pellets
from bosch_ASDIIE.Git_egylet.solid_version.core.wallgenerator import Wallgenerator
from bosch_ASDIIE.Git_egylet.solid_version.core.visualizer import Visualizer
from bosch_ASDIIE.Git_egylet.solid_version.gui.console_canvas import ConsoleCanvas
from bosch_ASDIIE.Git_egylet.solid_version.core.map import MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.screen import Screen
from bosch_ASDIIE.Git_egylet.solid_version.core.score import Score
from bosch_ASDIIE.Git_egylet.solid_version.core.terminate import Terminate
