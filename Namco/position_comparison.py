import numpy as np
import os


class PositionComparison:
    def check_collision(self) -> [bool,bool]:
        """
        Checks whether Pacman picked up a dot and increases the score accordingly
        :return: wall collision flag (bool), dot collision flag (bool)
        """
        for dot in self.dots:
            if dot == tuple(self.pacman):
                # If Pacman moved on a dot, increase the score and remove the dot
                self.dot_collision
                self.dots.remove(dot)

        for wall in self.wall:
            if wall == tuple(self.pacman):
                # If Pacman moved on a wall, terminate game
                self.wall_collision = true

        return self.wall_collision, self.dot_collision