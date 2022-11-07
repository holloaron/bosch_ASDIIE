from collections import deque
from typing import List

from Objects.core.canvas import Canvas
from Objects.core.get_action import KeyEvent
from Objects.core.map import Coordinates, MapSize
from Objects.core.pacman import Pacman
from Objects.gui.console_canvas import ConsoleCanvas


class SpyCanvas(Canvas):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._dots_on_canvas = []

    @property
    def dots_on_canvas(self):
        return self._dots_on_canvas

    def draw_dots(self, coordinates: List[Coordinates]):
        self._dots_on_canvas.extend(coordinates)
        self.canvas.draw_dots(coordinates)

    def clear(self):
        self._dots_on_canvas = []

    def render(self):
        pass


def testCanvas_whenPacmanHitTheEndOfCanvas_DoesNotDoAnything():
    """
    If Pacman reaches the wall (every side of map)  , can1t go forward
    """
    canvas = ConsoleCanvas(5, 5)
    spy_canvas = SpyCanvas(canvas)
    pacman = Pacman(
        Coordinates(0,3),
        starting_direction=KeyEvent.LEFT,
        map_size=MapSize(5, 5)
    )
    pacman.tick()
    pacman.tick()
    pacman.tick()
    pacman.tick()
    pacman.tick()
    pacman.tick()
    pacman.draw(spy_canvas)
    body_on_canvas = spy_canvas.dots_on_canvas
    assert Coordinates(0, 0) in body_on_canvas


