from collections import deque
from typing import Deque

from Objects.core.canvas import Canvas
from Objects.core.game_element import GameElement
from Objects.core.get_action import KeyEvent
from Objects.core.map import Coordinates, MapSize
from Objects.core.visualizable import Visualizable


class MovingTransformation:
    """
       A class for handling keyboard events during playing
       """

    def __init__(self, direction: KeyEvent, map_size: MapSize):
        self.direction = direction
        self.map_size = map_size

    def __call__(self, coordinates: Coordinates) -> Coordinates:
        if self.direction == KeyEvent.UP:
            new_row = (coordinates.row - 1)
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.LEFT:
            new_col = (coordinates.col - 1)
            return Coordinates(coordinates.row, new_col)
        elif self.direction == KeyEvent.DOWN:
            new_row = (coordinates.row + 1)
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.RIGHT:
            new_col = (coordinates.col + 1)
            return Coordinates(coordinates.row, new_col)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")


    def wall_limit(self, coordinates: Coordinates):
            """
            Limit pac-man to step outside the map.
            :param coordinates(Coordinates): pacman's desired position to step
            :return (Coordinates): allowed position
            """
            
            limited_x = max(1, min(coordinates.row, self.map_size.row_num))
            limited_y = max(1, min(coordinates.col, self.map_size.col_num))
            
            return Coordinates(limited_x,limited_y)    

class Pacman(GameElement, Visualizable):

    """
      A game element and visualizable class, for handling snake movement mainly,
      but visualizing is also represented here
    """
    def __init__(self,
                 body: Coordinates = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = None):
        if body is None:
            self.body = Coordinates(0, 1)
        else:
            self.body = body
        if map_size is None:
            map_size = MapSize(10, 10)
        self.moving_transformation = MovingTransformation(starting_direction, map_size)
        self.life_counter = 100


    def take_action(self, key_event: KeyEvent):
        self.moving_transformation.direction = key_event

    def tick(self):
        self.life_counter = self.life_counter -1
        desired_action = self.moving_transformation(self.body)
        self.body = self.moving_transformation.wall_limit(desired_action)
        if self.life_counter != 0:
            return True
        else:
            print("Game over")
            return False


    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.body)