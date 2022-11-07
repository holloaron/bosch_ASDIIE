import numpy as np
import os


class PositionComparison:

    def check_collision(self, map, pacman_x: int, pacman_y: int) -> [bool, bool]:
        """
        Checks whether Pacman picked up a dot or hit a wall, changes flags accordingly
        :return: wall collision flag (bool), dot collision flag (bool)
        """
        dot_collision = False
        wall_collision = False

        if map[pacman_x][pacman_y] == '-' or map[pacman_x][pacman_y] == '|':
            wall_collision = True

        elif map[pacman_x][pacman_y] == 'x':
            dot_collision = True

        return wall_collision, dot_collision
