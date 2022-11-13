from typing import List, Tuple
import numpy as np

from core.misc.map import MapSize, Coordinates


class PositionGenerator:

    def __init__(self,
                 map_size: MapSize,
                 known_pos: List[Coordinates]):
        """

        :param map_size:
        :param known_pos:
        """
        self.map_size = map_size
        self.known_pos = known_pos

    def generate_pos(self, num_of_pos: int) -> Tuple[List[Coordinates], List[Coordinates]]:
        """

        :param num_of_pos:
        :return:
        """
        pos_list = []
        for pos_num in range(num_of_pos):
            pos = Coordinates(np.random.randint(self.map_size[0]), np.random.randint(self.map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(self.map_size[0]), np.random.randint(self.map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list, self.known_pos
