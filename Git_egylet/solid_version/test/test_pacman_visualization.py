from collections import deque
from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.gui.console_canvas import ConsoleCanvas

class SpyCanvas(Canvas):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._dots_on_canvas = []
