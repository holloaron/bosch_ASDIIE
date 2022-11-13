from typing import List
import numpy as np

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable


class Pellets(GameElement, Visualizable):
    """
    This class handles the creation and visualization of the pellets
    """
    def __init__(self,
                 map_size: MapSize = None,
                 number_pellets: int = 10,
                 ):
        if map_size is None:
            map_size = MapSize(10, 10)

        self.positions = self.make_pellets(number=number_pellets, map_size=map_size)

    def make_pellets(self, number: int, map_size: MapSize) -> List[Coordinates]:
        """
        This function creates pellets across the map
        :param number: The number of pellets to make
        :param map_size: The size of the map
        :return: A list of the coordinates of the pellets
        """
        pellet_positions = []
        for _ in range(number):
            position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            #TODO: if there's another object in the map, generate a new position
            #while screen(position) != " ":
                #position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pellet_positions.append(position)

        return pellet_positions

    def draw(self, canvas: Canvas):
        """
        This function is responsible for the visualization of the pellets
        :param canvas: The interface for visualization
        :return:
        """
        canvas.draw_dots(self.positions, 'pellets')

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        return True