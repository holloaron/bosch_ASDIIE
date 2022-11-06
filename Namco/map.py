import numpy as np

class Map:
    def __init__(self):
        """
        Map class: initializing the map with walls and dots
        """
        # Loading map from the .txt file
        self.updated_map = None
        self.empty_map = np.loadtxt("map.txt", dtype= str, delimiter=',')
        # Filling up the map with dots
        self.empty_map[self.empty_map == ' '] = 'o'
        self.filled_map = self.empty_map

    def update_map (self,x: int,y: int) -> np.ndarray:
        """
        Updates the map based on Pacman's position
        :return: updated map (np.ndarray)
        """
        self.filled_map[self.filled_map == '0'] = ' '
        self.filled_map[x][y] = '0'
        self.updated_map = self.filled_map
        return self.updated_map