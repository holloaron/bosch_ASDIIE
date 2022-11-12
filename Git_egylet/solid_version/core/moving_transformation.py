from bosch_ASDIIE.Git_egylet.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.map import Coordinates, MapSize


class MovingTransformation:
    """
    This class is for handling keyboard events during playing
    """
    def __init__(self, direction: KeyEvent, map_size: MapSize):
        self.direction = direction
        self.map_size = map_size

    def __call__(self, coordinates: Coordinates) -> Coordinates:
        if self.direction == KeyEvent.UP:
            if coordinates.row - 1 < 0:
                new_row = self.map_size.row_num
            else:
                new_row = coordinates.row - 1
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.LEFT:
            if coordinates.col - 1 < 0:
                new_col = self.map_size.col_num
            else:
                new_col = coordinates.col - 1
            return Coordinates(coordinates.row, new_col)
        elif self.direction == KeyEvent.DOWN:
            if coordinates.row + 1 == self.map_size.row_num:
                new_row = 0
            else:
                new_row = coordinates.row + 1
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.RIGHT:
            if coordinates.col + 1 == self.map_size.col_num:
                new_col = 0
            else:
                new_col = coordinates.col + 1
            return Coordinates(coordinates.row, new_col)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")