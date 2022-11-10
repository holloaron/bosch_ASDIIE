from typing import List
import numpy as np

from bosch_ASDIIE.Git_egylet.solid_version.core.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.visualizable import Visualizable
from bosch_ASDIIE.Git_egylet.solid_version.core.screen import Screen


class Pellets(GameElement, Visualizable):
    """
    A visualizable class, for handling Pellets
    """
    def __init__(self,
                 map_size: MapSize = None,
                 number_pellets: int = 10,
                 ):
        if map_size is None:
            map_size = MapSize(10, 10)

        self.positions = self.make_pellets(number=number_pellets, map_size=map_size)

    def make_pellets(self, number: int, map_size: MapSize, screen: Screen) -> List[Coordinates]:
        pellet_positions = []
        for _ in range(number):
            position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            #TODO: if there's another object in the map, generate a new position
            #while screen(position) != " ":
                #position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pellet_positions.append(position)

        return pellet_positions

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.positions)

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        return True