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
        self.pos = tuple()

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

        state = self.update_map(state)

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

    def pos_generator(self, obj, num_objects):
        """
        This function generates (x, y) coordinate pairs randomly in the available spots.
        :param obj: name of the object to be generated across the map
        :param num_objects: number of objects for coordinates
        :return: None
        """
        for _ in range(num_objects):
            pos = tuple(np.random.randint(MAP_SIZE, size=(2, 1)))
            while pos in self.coins or pos in self.pos or pos in self.ghosts:
                pos = tuple(np.random.randint(MAP_SIZE, size=(2, 1)))

            if obj == 'ghost':
                self.ghosts.append(pos)
            elif obj == 'coin':
                self.coins.append(pos)
            elif obj == 'self_pos':
                self.pos = pos
            else:
                raise ValueError

    def update_map(self, state):
        """
        This function updates the game state given as input according to the coordinates included in tuples and returns
        the update-et array.
        :param state: current game state given as a numpy array with size=(MAP_SIZE, MAP_SIZE)
        :return: updated numpy array
        """
        for coin_pos in self.coins:
            state[coin_pos[0], coin_pos[1]] = 0.25

        for ghost_pos in self.ghosts:
            state[ghost_pos[0], ghost_pos[1]] = 0.5

        state[self.pos[0], self.pos[1]] = 1

        return state
