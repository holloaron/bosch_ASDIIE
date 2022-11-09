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

    def update_map(self, agent_pos: [int, int], done: bool) -> np.ndarray:
        """
        Updates the map based on PacMan's position
        :param agent_pos: x and y coordinate of the agent (int, int)
        :param done: game over flag (bool)
        :return: updated map (np.ndarray)
        """
        x = agent_pos[0]
        y = agent_pos[1]

        # PacMan's previous position must be emptied
        self.map[self.map == '0'] = ' '
        # PacMan should be placed into its current position
        self.map[x][y] = '0'
        # Marking place of death on map
        if done:
            self.map[self.map == '0'] = 'X'

        return self.map

    def check_collision(self, agent_pos: [int, int]) -> [bool, bool]:
        """
        Checks whether Pacman interacted with any objects on the map
        :return: wall collision flag (bool), dot collision flag (bool)
        """
        dot_collision = False
        wall_collision = False

        x = agent_pos[0]
        y = agent_pos[1]

        # Checking whether PacMan stepped on a wall
        if self.map[x][y] == '-' or self.map[x][y] == '|':
            wall_collision = True
        # Checking whether PacMan collected an eatable dot
        elif self.map[x][y] == 'x':
            dot_collision = True

        return dot_collision, wall_collision
