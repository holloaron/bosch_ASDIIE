from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates


class Walls(GameElement, Visualizable):

    def __init__(self,
                 map_size: MapSize = MapSize(10, 10),
                 internal_walls: List[Coordinates] = None,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """

        :param map_size:
        :param internal_walls:
        :param known_pos:
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        self.pos = self.generate_pos(map_size=map_size)

        if internal_walls is not None:
            self.pos = self.append_internal_pos(internal_walls)

    def take_action(self, key_event: KeyEvent) -> None:
        """

        """
        pass

    def tick(self, pacman_position: Coordinates) -> bool:
        """

        :return:
        """
        if pacman_position in self.pos:
            return False

        return True

    def draw(self, canvas: Canvas) -> None:
        """

        :param canvas:
        :return: None
        """
        canvas.draw_dots(self.pos, 'walls')

    @staticmethod
    def generate_pos(map_size: MapSize) -> List[Coordinates]:
        """

        :param map_size:
        :return:
        """
        pos_list = []
        for num_row in range(map_size.row_num):
            pos_list.append(Coordinates(num_row, 0))
            pos_list.append(Coordinates(num_row, map_size.col_num - 1))

        for num_col in range(1, map_size.col_num - 1):
            pos_list.append(Coordinates(0, num_col))
            pos_list.append(Coordinates(map_size.row_num - 1, num_col))

        return pos_list

    def append_internal_pos(self, pos: List[Coordinates]) -> List[Coordinates]:
        pos_list = self.pos

        for coordinate in pos:
            if coordinate not in self.known_pos:
                pos_list.append(coordinate)

        return pos_list
