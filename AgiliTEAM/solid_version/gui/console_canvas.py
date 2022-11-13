import os
from typing import List

from core.misc.map import Coordinates, MapSize
from core.interface.canvas import Canvas
from core.display.screen import Screen
from core.display.object_markers import ObjectMarkers


class ConsoleCanvas(Canvas):

    OBJECT_MARKERS = {
        "walls": ObjectMarkers.WALLS,
        "pacman": ObjectMarkers.PACMAN,
        "ghosts": ObjectMarkers.GHOSTS,
        "pellets": ObjectMarkers.PELLETS,
    }

    def __init__(self,
                 map_size: MapSize,
                 curses_screen: Screen):
        """

        :param map_size:
        :param curses_screen:
        """
        self.width = map_size.col_num + 1
        self.height = map_size.col_num + 1
        self.crs_screen = curses_screen
        self.map = self._get_empty_map()

    def clear(self) -> None:
        """

        :return: None
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.map = self._get_empty_map()
        self.crs_screen.clear()

    def draw_dots(self, coordinates: List[Coordinates], obj_type: str = None) -> None:
        """

        :param coordinates:
        :param obj_type:
        :return: None
        """
        for dot in coordinates:
            self.map[dot.row][dot.col] = self.OBJECT_MARKERS[obj_type].value

    def render(self) -> None:
        """

        :return: None
        """
        for num_row, row in enumerate(self.map):
            self.crs_screen.addstr(num_row, 0, "".join(row) + "\n")
        self.crs_screen.refresh()

    def _get_empty_map(self) -> list:
        """

        :return:
        """
        screen = []
        for height_pos in range(self.height):
            screen.append([" "] * self.width)
        return screen

    def get_height(self) -> int:
        """

        :return:
        """
        return self.height

    def get_width(self) -> int:
        """

        :return:
        """
        return self.width
