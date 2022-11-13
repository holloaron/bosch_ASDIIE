from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates


class MovingTransformation:

    def __init__(self, direction: KeyEvent, map_size: MapSize, prohibited_pos: List[Coordinates] = None):
        """

        :param direction:
        :param map_size:
        """
        self.direction = direction
        self.map_size = map_size
        if prohibited_pos is not None:
            self.prohibited_pos = prohibited_pos
        else:
            self.prohibited_pos = []

    def __call__(self, coordinates: Coordinates) -> Coordinates:
        """

        :param coordinates:
        :return:
        """
        if self.direction == KeyEvent.UP:
            new_row = coordinates.row if coordinates.row - 1 < 0 else coordinates.row - 1
            new_pos = Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.LEFT:
            new_col = coordinates.col if coordinates.col - 1 < 0 else coordinates.col - 1
            new_pos = Coordinates(coordinates.row, new_col)
        elif self.direction == KeyEvent.DOWN:
            new_row = coordinates.row if coordinates.row + 1 == self.map_size.row_num else coordinates.row + 1
            new_pos = Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.RIGHT:
            new_col = coordinates.col if coordinates.col + 1 == self.map_size.col_num else coordinates.col + 1
            new_pos = Coordinates(coordinates.row, new_col)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")

        if new_pos not in self.prohibited_pos:
            return new_pos
        else:
            return coordinates
