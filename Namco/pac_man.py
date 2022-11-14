import numpy as np


class PacMan:
    def __init__(self, x: int = 0, y: int = 0):
        """
        Implements PacMan
        :param x: row that PacMan starts the game at
        :param y: col that PacMan starts the game at
        """
        self.x = x
        self.y = y

    def process_action(self, action: str):
        """
        Moves PacMan in the desired direction
        :param action: current user input (w, a, s or d) (str)
        :return: Current x and y coordinate of PacMan [int, int]
        """
        # Moving up
        if action == 'w':
            self.x -= 1
        # Moving left
        elif action == 'a':
            self.y -= 1
        # Moving down
        elif action == 's':
            self.x += 1
        # Moving right
        elif action == 'd':
            self.y += 1

    def generate_init_pos(self, _map: np.ndarray, map_size: int, restricted_slot: str):
        """
        Determining the agent's initial position to a non-restricted area
        :return: -
        """
        while _map[self.x][self.y] == restricted_slot:
            self.x = np.random.randint(map_size)
            self.y = np.random.randint(map_size)

    @property
    def position(self):
        """
        Returns PacMan's current x and y coordinate
        :return: x and y coordinate of PacMan
        """
        return self.x, self.y
