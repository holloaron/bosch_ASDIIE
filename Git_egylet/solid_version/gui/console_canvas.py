import os
from typing import List

from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.canvas import Canvas
from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.screen import Screen


class ConsoleCanvas(Canvas):
    def __init__(self, map_size: MapSize, curses_screen: Screen):
        self.width = map_size.col_num + 1
        self.height = map_size.col_num + 1
        self.crs_screen = curses_screen
        self.map = self._get_empty_map()