from collections import deque
from typing import Deque

from bosch_ASDIIE.solid_version.core.game_element import GameElement
from bosch_ASDIIE.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.solid_version.core.map import Coordinates


class MovingTransformation:
    """
    A class for handling keyboard events during playing
    """
    def __init__(self, direction: KeyEvent):
        self.direction = direction

    def set_direction(self, new_direction):
        self.direction = new_direction

    def __call__(self, coodinates: Coordinates) -> Coordinates:
        if self.direction == KeyEvent.UP:
            return Coordinates(coodinates.row - 1, coodinates.col)
        elif self.direction == KeyEvent.LEFT:
            return Coordinates(coodinates.row, coodinates.col - 1)
        elif self.direction == KeyEvent.DOWN:
            return Coordinates(coodinates.row + 1, coodinates.col)
        elif self.direction == KeyEvent.RIGHT:
            return Coordinates(coodinates.row, coodinates.col + 1)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")


class Snake(GameElement):
    """
    A game element class, for handling snake movement mainly
    """
    def __init__(self, body: Deque[Coordinates] = None, starting_direction: KeyEvent = KeyEvent.RIGHT):
        if body is None:
            self.body_parts = deque([
                Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3),
                Coordinates(0, 4), Coordinates(0, 5)
            ])
        else:
            self.body_parts = body
        self.moving_transformation = MovingTransformation(starting_direction)

    def take_action(self, key_event: KeyEvent):
        self.moving_transformation.set_direction(key_event)

    def tick(self):
        self.body_parts.popleft()
        new_head = self.moving_transformation(self.body_parts[-1])
        if new_head in self.body_parts:
            return False
        self.body_parts.append(new_head)
        return True