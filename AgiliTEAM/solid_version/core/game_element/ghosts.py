from typing import List
import numpy as np
import math
import random

from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.move import MovingTransformation
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates


class Ghosts(GameElement, Visualizable):

    GHOST_START_DIRECTION = KeyEvent.RIGHT

    def __init__(self,
                 map_size: MapSize = None,
                 num_ghosts: int = 4,
                 known_pos: List[List[Coordinates]] = None,
                 step_confidence: float = 0.8,
                 ):
        """

        :param map_size:
        :param num_ghosts:
        :param known_pos:
        :param step_confidence:
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if map_size is None:
            map_size = MapSize(10, 10)
        self.step_confidence = step_confidence
        self.event = self.GHOST_START_DIRECTION
        self.pos = self.generate_pos(num_of_pos=num_ghosts, map_size=map_size)
        self.moving_transformation_ghost = MovingTransformation(self.event, map_size)

    def generate_pos(self, num_of_pos: int, map_size: MapSize) -> List[Coordinates]:
        """

        :param num_of_pos:
        :param map_size:
        :return:
        """
        pos_list = []
        for _ in range(num_of_pos):
            pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list

    def __take_best_action__(self, pacman_position: Coordinates, ghost_index: int):
        """

        :param pacman_position:
        :param ghost_index:
        :return:
        """
        current_ghost_pos = self.pos[ghost_index]
        ghost_pacman_angle = math.atan2((pacman_position.row - current_ghost_pos.row),
                                        (pacman_position.col - current_ghost_pos.col))
        direction_component_in_x = math.cos(ghost_pacman_angle)
        direction_component_in_y = math.sin(ghost_pacman_angle)
        is_it_vertical_step = True if abs(direction_component_in_x) < abs(direction_component_in_y) else False
        greater_direction_component = direction_component_in_y if abs(direction_component_in_x) < abs(
            direction_component_in_y) else direction_component_in_x

        if 0 > greater_direction_component and is_it_vertical_step:
            self.event = KeyEvent.UP
        elif 0 < greater_direction_component and is_it_vertical_step:
            self.event = KeyEvent.DOWN
        elif 0 > greater_direction_component and not is_it_vertical_step:
            self.event = KeyEvent.LEFT
        elif 0 < greater_direction_component and not is_it_vertical_step:
            self.event = KeyEvent.RIGHT

        self.moving_transformation_ghost.direction = self.event
        self.pos[ghost_index] = self.moving_transformation_ghost(self.pos[ghost_index])

    def __take_random_action__(self, ghost_index: int) -> None:
        """

        :param ghost_index:
        :return:
        """
        self.event = random.randrange(1, 4)
        self.pos[ghost_index] = self.moving_transformation_ghost(self.pos[ghost_index])

    def take_action(self, pacman_position: Coordinates) -> None:
        """

        :param pacman_position:
        :return: None
        """
        for idx in range(len(self.pos)):
            if random.uniform(0, 1) >= self.step_confidence:
                self.__take_best_action__(pacman_position, idx)
            else:
                self.__take_random_action__(idx)

    def tick(self, pacman_position: Coordinates) -> bool:
        """

        :param pacman_position:
        :return:
        """
        self.take_action(pacman_position)
        return True

    def draw(self, canvas: Canvas) -> None:
        """

        :param canvas:
        :return: None
        """
        canvas.draw_dots(self.pos, 'ghosts')
