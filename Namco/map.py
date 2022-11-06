import numpy as np

class Map:
    def __init__(self):
        # Loading map from the .txt file
        self.empty_map = np.loadtxt("map.txt", dtype= str, delimiter=',')
        # Filling up the map with dots
        self.filled_map= self.empty_map[self.empty_map == ' '] = 'o'
        # for line in self.empty_map:
        #    print(*line, sep='  ')
    def return_map (self):
        """
        Updates the map based on Pacman's position
        :return: updated map (list(list(str)))
        """
        return self.filled_map

env = Map()
filled_map = env.return_map()
