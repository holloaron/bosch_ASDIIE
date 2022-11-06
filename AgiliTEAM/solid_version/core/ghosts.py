from typing import List
import numpy as np

from solid_version.core.key_event import KeyEvent
from solid_version.core.game_element import GameElement
from solid_version.core.visualizable import Visualizable
from solid_version.core.canvas import Canvas
from solid_version.core.map import MapSize, Coordinates


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

        self.pos = self.generate_pos(num_of_pos=num_ghosts, map_size=map_size)

    def generate_pos(self, num_of_pos: int, map_size: MapSize) -> List[Coordinates]:
        pos_list = []
        for _ in range(num_of_pos):
            pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list

    def take_action(self, key_event: KeyEvent, pacman_position: Coordinates):
        # TODO: ghost moves

        pass

    def tick(self) -> bool:
        return True

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.pos, 'ghosts')
