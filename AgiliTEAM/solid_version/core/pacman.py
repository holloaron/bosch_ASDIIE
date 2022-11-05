import numpy as np
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.move import MovingTransformation
from bosch_ASDIIE.AgiliTEAM.solid_version.core.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.map import MapSize, Coordinates


class Pacman(GameElement, Visualizable):

    def __init__(self,
                 body: List[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = None,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if map_size is None:
            map_size = MapSize(10, 10)

        if body is None:
            self.pos = self.generate_pos(1, map_size)
        else:
            self.pos = body

        self.moving_transformation = MovingTransformation(starting_direction, map_size)

    def take_action(self, key_event: KeyEvent):
        if self._is_not_opposite_direction(key_event):
            self.moving_transformation.direction = key_event

    def tick(self):
        self.body_parts.popleft()
        new_head = self.moving_transformation(self.body_parts[-1])
        if new_head in self.body_parts:
            return False
        self.body_parts.append(new_head)
        return True

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.body_parts)

    def _is_not_opposite_direction(self, key_event):
        if self.moving_transformation.direction == KeyEvent.LEFT and \
                key_event == KeyEvent.RIGHT:
            return False
        if self.moving_transformation.direction == KeyEvent.RIGHT and \
                key_event == KeyEvent.LEFT:
            return False
        if self.moving_transformation.direction == KeyEvent.UP and \
                key_event == KeyEvent.DOWN:
            return False
        if self.moving_transformation.direction == KeyEvent.DOWN and \
                key_event == KeyEvent.UP:
            return False
        return True