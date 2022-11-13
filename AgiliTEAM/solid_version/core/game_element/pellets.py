from typing import List
import numpy as np

from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.pos_generator import PositionGenerator


class Pellets(GameElement, Visualizable):

    def __init__(self,
                 map_size: MapSize = MapSize(10, 10),
                 num_pellets: int = 10,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """

        :param map_size:
        :param num_pellets:
        :param known_pos:
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        pos_generator = PositionGenerator(map_size, self.known_pos)

        self.pos = self.generate_pos(num_of_pos=num_pellets, map_size=map_size)

    def generate_pos(self, num_of_pos: int, map_size: MapSize) -> List[Coordinates]:
        pos_list = []
        for _ in range(num_of_pos):
            pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        """

        """
        return True

    def draw(self, canvas: Canvas) -> None:
        """

        :param canvas:
        :return: None
        """
        canvas.draw_dots(coordinates=self.pos, obj_type='pellets')
