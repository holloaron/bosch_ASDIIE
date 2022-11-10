import os
from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.screen import Screen


class ConsoleCanvas(Canvas):
    def __init__(self, map_size: MapSize, curses_screen: Screen):
        self.width = map_size.col_num + 1
        self.height = map_size.col_num + 1
        self.crs_screen = curses_screen
        self.map = self._get_empty_map()

    def clear(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.map = self._get_empty_map()
        self.crs_screen.clear()

    def draw_dots(self, coordinates: List[Coordinates]):
        for dot in coordinates:
            self.map[dot.row][dot.col] = "x"

    def draw_walls(self, coordinates: List[Coordinates]):
        for wall in coordinates:
            self.map[wall.row][wall.col] = "x"

    def render(self):
        for num_row, row in enumerate(self.map):
            self.crs_screen.addstr(num_row, 0, "".join(row) + "\n")
        self.crs_screen.refresh()

    def _get_empty_map(self):
        screen = []
        for _ in range(self.height):
            screen.append([" "] * self.width)
        return screen

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width