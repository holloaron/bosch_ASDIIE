import numpy as np


class Map:
    def __init__(self, map_source: str = "map.txt"):
        """
        :param map_source: name of the map file (str)
        Map class: initializing the map with walls and dots
        """
        # Loading map from the .txt file
        self.map = None
        self.map = np.loadtxt(map_source, dtype=str, delimiter=',')
        # Filling up the map with dots
        self.map[self.map == ' '] = 'x'

    def update_map(self, x: int, y: int) -> np.ndarray:
        """
        Updates the map based on Pacman's position
        :param x: Pacman's x position (int)
        :param y: Pacman's y position (int)
        :return: updated map (np.ndarray)
        """
        self.map[self.map == '0'] = ' '
        self.map[x][y] = '0'
        return self.map
