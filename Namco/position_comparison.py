import numpy as np
import os

EMPTY = 0
PACMAN = 1
DOT = 2
WALL = 3


class PositionComparison:
    def __init__(self, ):


    def create_observation(self) -> np.ndarray:
        """
        Processes the positions of Pacman and the edible dots and creates the current state matrix
        :return: Current state of the map (np.ndarray)
        """
        # Creating the map
        observation = np.zeros((self.map_size, self.map_size), dtype=int)

        # Placing Pacman on the map
        observation[self.pacman[0], self.pacman[1]] = PACMAN

        # Placing the edible dots on the map
        for dot in self.dots:
            observation[dot[0], dot[1]] = DOT

        return observation

    def check_dots(self) -> None:
        """
        Checks whether Pacman picked up a dot and increases the score accordingly
        :return: -
        """
        for dot in self.dots:
            if dot == tuple(self.pacman):
                # If Pacman moved on a dot, increase the score and remove the dot
                self.score += 1
                self.dots.remove(dot)

