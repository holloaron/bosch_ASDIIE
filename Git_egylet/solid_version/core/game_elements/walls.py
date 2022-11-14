from typing import List
import numpy as np

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable


class Walls(GameElement, Visualizable):
    """
    This class is responsible for the creation and visualization of the walls
    """
    def __init__(self,
                 map_size: MapSize = None,
                 number_walls: int = 10,
                 ):
        if map_size is None:
            map_size = MapSize(10, 10)

        self.positions = self.make_walls(number=number_walls, map_size=map_size)

    def make_walls(self, number: int, map_size: MapSize) -> List[Coordinates]:
        """
        This function is responsible for creating walls across the map
        :param number: The number of walls to create
        :param map_size: The size of the map
        :return: A list of the coordinates of the walls
        """
        wall_positions = []
        for _ in range(number):
            position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            wall_positions.append(position)

        return wall_positions

    def draw(self, canvas: Canvas):
        """
        This class is responsible for the visualization of the walls
        :param canvas: The interface for visualization
        :return:
        """
        canvas.draw_dots(self.positions, 'walls')

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        return True