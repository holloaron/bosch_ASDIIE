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
        # variables for world
        self.show_window_size = 300
        self.show_window = np.zeros((self.show_window_size, self.show_window_size, 3))
        self.ratio = int(self.show_window_size / self.world_size)
        self.reset()

    def step(self, action):
        # set default score
        score = 0
        # set basic status
        done = False
        # get the current PacMan position
        pos_x, pos_y = self.body[-1]

        x, y = self._move(pos_x, pos_y, action)

        # add current state to the body
        if (x, y) not in self.body:
            self.body.append((x, y))

        obs = self._create_observation()
        self.last_state = obs

        # check for pellets
        # if (x, y) in self.pellets: todo: function for event when pacman collides with pellets

        self.step_counter += 1

        done = self.is_done(self.max_steps)

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

    def create_pellets(self, numbers):
        for _ in range(numbers):
            coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            while coordinates in self.pellets or coordinates in self.body:
                coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            self.pellets.append(coordinates)

    def _move(self, pos_x, pos_y, action):
        self.direction = self._change_direction(action)
        if self.direction == 0:
            x, y = self._up(pos_x, pos_y)
        elif self.direction == 1:
            x, y = self._right(pos_x, pos_y)
        elif self.direction == 2:
            x, y = self._down(pos_x, pos_y)
        elif self.direction == 3:
            x, y = self._left(pos_x, pos_y)
        return x, y

    def _change_direction(self, action):
        if 0 <= action < 4:
            self.direction = action
        else:
            raise ValueError("Please choose an action between 0-3")

    def _up(self, pos_x, pos_y):
        pos_y += 1
        return pos_x, pos_y

    def _right(self, pos_x, pos_y):
        pos_x += 1
        return pos_x, pos_y

    def _down(self, pos_x, pos_y):
        pos_y -= 1
        return pos_x, pos_y

    def _left(self, pos_x, pos_y):
        pos_x -= 1
        return pos_x, pos_y

    def _create_observation(self):

        obs_ = np.zeros((self.world_size, self.world_size, 1))

        for pellet in self.pellets:
            obs_[pellet[0], pellet[1], 0] = 0.25

        obs_[self.body[0], self.body[1], 0] = 0.8
        return obs_

    def render(self):
        if self.last_state is not None:
            img = np.float32(self.last_state)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        for i in range(self.show_window_size):
            for j in range(self.show_window_size):
                self.show_window[i][j] = img[i // self.ratio][j // self.ratio]
        cv2.imshow("Pacman", self.show_window)
        cv2.waitKey(50)

    def reset(self):
        self.body = []
        self.pellets = []
        self.step_counter = 0
        self.direction = 1
        self.score = 0
        self.last_state = None

        self.create_pacman()
        self.create_pellets(10)
        obs_ = self._create_observation()
        return obs_.flatten()


if __name__ == "__main__":
    env = Pacman(world_size=1)
    done = False
    state = env.reset()
    while not done:
        a = int(input("Choose your next action:\n"))
        state, reward, done, info = env.step(action=a)
        env.render()
