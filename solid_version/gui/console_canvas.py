import os
from typing import List

from bosch_ASDIIE.solid_version.core.map import Coordinates
from bosch_ASDIIE.solid_version.core.canvas import Canvas


class ConsoleCanvas(Canvas):
    """
    The canvas class for the console version
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = self._get_empty_screen()
    
    def clear(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.screen = self._get_empty_screen()
    
    def draw_dots(self, coordinates: List[Coordinates]):
        for dot in coordinates:
            self.screen[dot.row][dot.col] = "x"
        
    def render(self):
        screen_to_plot = ""
        for row in self.screen:
            screen_to_plot += "".join(row) + "\n"
        print(screen_to_plot)

    def _get_empty_screen(self):
        screen = []
        for _ in range(self.height):
            screen.append([" "] * self.width)
        return screen