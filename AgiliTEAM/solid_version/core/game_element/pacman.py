import numpy as np
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.move import MovingTransformation
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.pos_generator import PositionGenerator


class Pacman(GameElement, Visualizable):

    def __init__(self,
                 body: List[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = MapSize(10, 10),
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """

        :param body:
        :param starting_direction:
        :param map_size:
        :param known_pos:
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if body is None:
            pos_generator = PositionGenerator(map_size, self.known_pos)
            self.pos, self.known_pos = pos_generator.generate_pos(1)
        else:
            self.pos = body

        self.moving_transformation = MovingTransformation(starting_direction, map_size)

    def take_action(self, key_event: KeyEvent) -> None:
        """

        :param key_event:
        :return: None
        """
        self.moving_transformation.direction = key_event

    def get_pacman_position(self) -> Coordinates:
        """

        :return:
        """
        return self.pos[0]

    def tick(self) -> bool:
        """

        :return:
        """
        self.pos = [self.moving_transformation(self.pos[0])]
        return True

    def draw(self, canvas: Canvas) -> None:
        """

        :param canvas:
        :return: None
        """
        canvas.draw_dots(self.pos, 'pacman')
