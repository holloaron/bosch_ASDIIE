import numpy as np


class Map:
    def __init__(self, map_source: str = "map.txt"):
        """
        :param map_source: name of the map file (str)
        Map class: initializing the map with walls and dots
        """
        # Loading map from the .txt file
        self.map = np.loadtxt(map_source, dtype=str, delimiter=',')
        # Filling up the map with dots
        self.map[self.map == ' '] = 'x'

    def update_map(self, pacman_x: int, pacman_y: int, done: bool) -> np.ndarray:
        """
        Updates the map based on PacMan's position
        :param pacman_x: PacMan's x position (int)
        :param pacman_y: PacMan's y position (int)
        :param done: Game over flag (bool)
        :return: updated map (np.ndarray)
        """
        # PacMan's previous position must be emptied
        self.map[self.map == '0'] = ' '
        # PacMan should be placed into its current position
        self.map[pacman_x][pacman_y] = '0'
        if done:
            self.map[self.map == '0'] = 'X'
        return self.map
