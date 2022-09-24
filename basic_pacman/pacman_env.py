from typing import Tuple
import cv2
import numpy as np
np.random.seed(0)

MAP_SIZE = 30
MAX_STEP = 100
NUM_GHOSTS = 4
NUM_COINS = 100
ACTION_SPACE_SIZE = 4


class Pacman:
    """

    """
    def __init__(self) -> None:
        """
        Constructs the basic components of the Pacman Environment Class.
        :return: None
        """
        self.map_size = MAP_SIZE

        self.coins_pos = []
        self.ghosts_pos = []
        self.pos = tuple()

        self.step_counter = None
        self.score = None
        self.orientation = None

        self.state = self.reset()

    def reset(self):
        """
        This function resets the game session and returns a newly generated game state.
        :return: current state of the game (empty map with the pacman, ghosts and coins spawned)
        """
        self.step_counter = 0
        self.score = 0
        self.orientation = np.random.randint(4)

        self.ghosts_pos = []
        self.coins_pos = []

        self._generate_pos('self_pos', 1)
        self._generate_pos('ghost', NUM_GHOSTS)
        self._generate_pos('coin', NUM_COINS)

        state = self.update_map()

        return state

    def __move(self):
        if self.orientation == 0:
            self.pos[0] -= 1
        if self.orientation == 1:
            self.pos[1] += 1
        if self.orientation == 2:
            self.pos[0] += 1
        if self.orientation == 3:
            self.pos[1] -= 1

        return self.pos

    def step(self, action):
        """
        This function realizes the change in the game state according to the chosen action.
        :param action: chosen action (integer 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return: (state, reward, done, info)
        """
        if 0 <= action < 4:
            self.orientation = action
        else:
            raise ValueError

        self.pos = self.__move()
        self.step_cnt += 1

        reward = 0

        done = self._check_done()

        self._calculate_score()
        info = "Points acquired: " + str(self.score)

        self.state = self.update_map()

        return self.state, reward, done, info

    def _calculate_score(self):
        """
        This function calculates the scores which may have been acquired during the last step, and if so, removes the
        coin from the map.
        :return: None
        """
        for coin_pos in self.coins_pos:
            if self.pos == coin_pos:
                self.score += 10
                self.coins_pos.remove(coin_pos)

    def _check_done(self):
        """
        This function analyzes the game state and decides whether it's terminated or not.
        :return: 'done' boolean value
        """
        if self.step_counter > MAX_STEP:
            return True

        for ghost_pos in self.ghosts_pos:
            if self.pos == ghost_pos:
                return True

        return False

    def render(self):
        """
        This function creates a visualization window of the current state.
        :return: None
        """
        print(self.state)
        self.state[self.pos[0]][self.pos[1]] = 1
        print(self.state)

    def pos_generator(self, obj, num_objects):
        """
        This function generates (x, y) coordinate pairs randomly in the available spots.
        :param obj: name of the object to be generated across the map
        :param num_objects: number of objects for coordinates
        :return: None
        """
        for _ in range(num_objects):
            pos = list(np.random.randint(MAP_SIZE, size=(2,)))
            while pos in self.coins_pos or pos == self.pos or pos in self.ghosts_pos:
                pos = list(np.random.randint(MAP_SIZE, size=(2,)))

            if obj == 'ghost':
                self.ghosts_pos.append(pos)
            elif obj == 'coin':
                self.coins_pos.append(pos)
            elif obj == 'self_pos':
                self.pos = pos
            else:
                raise ValueError

    def update_map(self):
        """
        This function updates the game state given as input according to the coordinates included in tuples and returns
        the update-et array.
        :return: updated numpy array
        """
        state = np.zeros((MAP_SIZE, MAP_SIZE))

        for coin_pos in self.coins_pos:
            state[coin_pos[0], coin_pos[1]] = 0.25

        for ghost_pos in self.ghosts_pos:
            state[ghost_pos[0], ghost_pos[1]] = 0.5

        state[self.pos[0], self.pos[1]] = 1

        return state
