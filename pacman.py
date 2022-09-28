"""""
created by Git-egylet
"""""

import cv2
import numpy as np

class Pacman:
    def __init__(self, world_size):
        self.world_size = world_size
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

        # get new PacMan position
        if self.direction == 0:
            x, y, = self._up(action, pos_x, pos_y)
        elif self.direction == 1:
            x, y, = self._right(action, pos_x, pos_y)
        elif self.direction == 2:
            x, y, = self._down(action, pos_x, pos_y)
        elif self.direction == 3:
            x, y, = self._left(action, pos_x, pos_y)
        else:
            raise NotImplementedError

        # wall collision check
        x = self.__check_walls(x)
        y = self.__check_walls(y)

        # add current state to the body
        if (x, y) not in self.body:
            self.body.append((x, y))

        # check for pellets
        # if (x, y) in self.pellets: todo: function for event when pacman collides with pellets

        self.step_counter += 1
