import numpy as np
import os


class PositionComparison:

    dot_collision = False
    wall_collision = False
    def check_collision(self) -> [bool,bool]:
        """
        Checks whether Pacman picked up a dot and increases the score accordingly
        :return: wall collision flag (bool), dot collision flag (bool)
        """
        for dot in self.dots:
            if dot == tuple(self.pacman):
                # If Pacman moved on a dot, increase the score and remove the dot
                dot_collision = True
                self.dots.remove(dot)

        for wall in self.wall:
            if wall == tuple(self.pacman):
                # If Pacman moved on a wall, terminate game
                wall_collision = True

        return self.wall_collision, self.dot_collision