from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable
from bosch_ASDIIE.Git_egylet.solid_version.core.move.moving_transformation import MovingTransformation


class Pacman(GameElement, Visualizable):
    """
    This class handles the visualization of the PacMan and its movement
    """
    def __init__(self,
                 body: List[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = None):
        if body is None:
            self.position = Coordinates(0, 1)
        else:
            self.position = body
        if map_size is None:
            map_size = MapSize(10, 10)
        self.moving_transformation = MovingTransformation(starting_direction, map_size)

    def take_action(self, key_event: KeyEvent):
        self.moving_transformation.direction = key_event

    def tick(self) -> bool:
        self.position = [self.moving_transformation(self.position[0])]
        return True

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.position, 'pacman')
