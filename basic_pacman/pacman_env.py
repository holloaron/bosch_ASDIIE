import numpy as np
np.random.seed(0)

MAP_SIZE = 30


class Pacman:
    """

    """
    def __init__(self):
        self.map_size = MAP_SIZE

        self.coins = []
        self.ghosts = []
        self.pos = None

        self.step = None
        self.score = None
        self.orientation = None

        self.state = self.reset()

    def reset(self):
        """
        This function resets the game session and returns a newly generated game state.
        :return: current state of the game (empty map with the pacman, ghosts and coins spawned)
        """
        state = np.zeros((MAP_SIZE, MAP_SIZE))

        self.step = 0
        self.score = 0
        self.orientation = np.random.randint(4)

        self.ghosts = []
        self.coins = []

        self.pos_generator('self_pos', 1)
        self.pos_generator('ghost', 4)
        self.pos_generator('coin', 300)

        self.update_map(state)

        return state

    def step(self, a):
        """
        This function realizes the change in the game state according to the chosen action.
        :param a: chosen action (integer 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return: (state, reward, done, info)
        """
        raise NotImplementedError

    def render(self):
        """
        This function creates a visualization window of the current state.
        :return: None
        """
        raise NotImplementedError
