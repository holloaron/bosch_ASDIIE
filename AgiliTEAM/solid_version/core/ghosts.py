from typing import List
import numpy as np
import math

from solid_version.core.key_event import KeyEvent
from solid_version.core.game_element import GameElement
from solid_version.core.visualizable import Visualizable
from solid_version.core.move import MovingTransformation
from solid_version.core.canvas import Canvas
from solid_version.core.map import MapSize, Coordinates

GHOST_START_DIRECTION = KeyEvent.RIGHT


class Ghosts(GameElement, Visualizable):

    def __init__(self,
                 map_size: MapSize = None,
                 num_ghosts: int = 4,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if map_size is None:
            map_size = MapSize(10, 10)

        self.event = GHOST_START_DIRECTION
        self.pos = self.generate_pos(num_of_pos=num_ghosts, map_size=map_size)
        self.moving_transformation_ghost = MovingTransformation(self.event, map_size)

    def generate_pos(self, num_of_pos: int, map_size: MapSize) -> List[Coordinates]:
        pos_list = []
        for _ in range(num_of_pos):
            pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list

    def take_action(self, pacman_position: Coordinates):
        for i in range(len(self.pos)):
            current_ghost_pos = self.pos[i]
            ghost_pacman_angle = math.atan2((pacman_position.row - current_ghost_pos.row),
                                            (pacman_position.col - current_ghost_pos.col))
            step_in_x = math.cos(ghost_pacman_angle)
            step_in_y = math.sin(ghost_pacman_angle)
            is_it_vertical_step = True if abs(step_in_x) < abs(step_in_y) else False
            greater_direction_component = step_in_y if abs(step_in_x) < abs(step_in_y) else step_in_x

            if 0 > greater_direction_component and is_it_vertical_step:
                self.event = KeyEvent.UP
            elif 0 < greater_direction_component and is_it_vertical_step:
                self.event = KeyEvent.DOWN
            elif 0 > greater_direction_component and not is_it_vertical_step:
                self.event = KeyEvent.LEFT
            elif 0 < greater_direction_component and not is_it_vertical_step:
                self.event = KeyEvent.RIGHT

            self.moving_transformation_ghost.direction = self.event
            self.pos[i] = self.moving_transformation_ghost(self.pos[i])

    def tick(self, pacman_position: Coordinates) -> bool:
        self.take_action(pacman_position)
        return True

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.pos, 'ghosts')
