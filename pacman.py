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
        self.step = 0
        self.direction = 1
        self.score = 0
        self.last_state = None
        # variables for world
        self.show_window_size = 300
        self.show_window_size = np.zeros((self.show_window_size, self.show_window_size, 3))
        self.ratio = int(self.show_window_size / self.world_size)
        self.reset()
        