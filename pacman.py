"""""
created by Git-egylet
"""""

import cv2
import numpy as np


class Pacman:
    def __init__(self, world_size):
        self.world_size = world_size
        self.max_steps = 200
        # map components list
        self.body = []
        self.walls = []
        self.ghosts = []
        self.pellets = []
        # default values
        self.step_counter = 0
        self.direction = 1
        self.score = 0
        self.last_state = None
        self.size = 3
        # variables for world
        self.show_window_size = 300
        self.show_window_size = np.zeros((self.show_window_size, self.show_window_size, 3))
        self.ratio = int(self.show_window_size / self.world_size)
        self.reset()

    def step(self, action):
        # set default score
        score = 0
        # set basic status
        done = False
        # get the current PacMan position
        pos_x, pos_y = self.body[-1]

        x, y = self._move(pos_x,pos_y,action)

        # add current state to the body
        if (x, y) not in self.body:
            self.body.append((x, y))

        # check for pellets
        # if (x, y) in self.pellets: todo: function for event when pacman collides with pellets

        self.step_counter += 1

        done = self.is_done()

    def is_done(self, max_steps: int):
        """
        This function checks if the game has reached the maximum amount of timesteps.
        :param max_steps: maximum amount of steps during the game
        :return: boolean value
        """
        if self.step_counter > max_steps:
            return True
        else:
            return False

    def create_pacman(self):
        self.body.append((0, 0))
        self.size = 3

    def create_pellets(self, numbers):
        for _ in range(numbers):
            coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            while coordinates in self.pellets or coordinates in self.body:
                coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            self.pellets.append(coordinates)

    def _move (self, pos_x, pos_y, action):
        raise NotImplementedError
