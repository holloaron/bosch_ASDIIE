import numpy as np
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.move import MovingTransformation
from bosch_ASDIIE.AgiliTEAM.solid_version.core.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.map import MapSize, Coordinates


    def __call__(self, coordinates: Coordinates) -> Coordinates:
        if self.direction == KeyEvent.UP:
            new_row = (coordinates.row - 1) % self.map_size.row_num
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.LEFT:
            new_col = (coordinates.col - 1) % self.map_size.col_num
            return Coordinates(coordinates.row, new_col)
        elif self.direction == KeyEvent.DOWN:
            new_row = (coordinates.row + 1) % self.map_size.row_num
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.RIGHT:
            new_col = (coordinates.col + 1) % self.map_size.col_num
            return Coordinates(coordinates.row, new_col)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")


class Snake(GameElement, Visualizable):
    """
    A game element and visualizable class, for handling snake movement mainly,
    but visualizing is also represented here
    """
    def __init__(self,
                 body: Deque[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = None):
        if body is None:
            self.body_parts = deque([
                Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3),
                Coordinates(0, 4), Coordinates(0, 5)
            ])
        else:
            self.body_parts = body
        if map_size is None:
            map_size = MapSize(10, 10)
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