"""
created by Laszlo Szoke
laszlo.szoke@hu.bosch.com
copied from https://github.com/bme-kjit/bosch_ASDIIE/blob/main/basic_version/snake.py
modified by Dávid Czuri
"""
import time
import cv2
import numpy as np
from pynput import keyboard


class Pacman:
    KEY_NAME_UP = 'up'
    KEY_NAME_DOWN = 'down'
    KEY_NAME_RIGHT = 'right'
    KEY_NAME_LEFT = 'left'

    DIRECTION_UP = 3
    DIRECTION_DOWN = 1
    DIRECTION_RIGHT = 0
    DIRECTION_LEFT = 2

    def __init__(self, map_size):
        self.map_size = map_size
        # lists for the map components
        self.body = []
        self.collectables = []
        # initiate default values
        self.steps_ = 0
        self.direction = 1
        self.size = 1
        self.last_observation = None
        # Variables for visualizing the current grid world
        self.displayed_img_size = 300
        self.displayed_img = np.zeros((self.displayed_img_size, self.displayed_img_size, 3))
        self.image_to_map_size_ratio = int(self.displayed_img_size / self.map_size)
        self.reset()

    def step(self, direction):
        # setting base reward
        score = 0

        # setting basic env status
        is_dead = False
        # getting the current head position (always the last body part)
        position_x, position_y = self.body[-1]

        # get new head position
        if self.direction == 0:
            new_position_x, new_position_y, = self._move_up(direction, position_x, position_y)
        elif self.direction == 1:
            new_position_x, new_position_y, = self._move_right(direction, position_x, position_y)
        elif self.direction == 2:
            new_position_x, new_position_y, = self._move_down(direction, position_x, position_y)
        elif self.direction == 3:
            new_position_x, new_position_y, = self._move_left(direction, position_x, position_y)
        else:
            raise NotImplementedError

        if self.position_is_out_of_map(new_position_x, new_position_y):
            new_position_x, new_position_y = self.move_to_the_other_side_of_the_map(new_position_x, new_position_x)

        # add current step to the body
        self.body.append((new_position_x, new_position_y))

        # checking for object to eat
        if (new_position_x, new_position_y) in self.collectables:
            score = 1
            self.collectables.remove((new_position_x, new_position_y))

        observation = self._create_observation()

        # save observation
        self.last_observation = observation

        self.steps_ += 1

        # terminating the game after some step
        if self.steps_ > 100:
            is_dead = True

        return observation.flatten(), score, is_dead

    def _move_right(self, initial_direction, position_x, position_y):
        # going up
        if initial_direction == 0:
            position_y += 1
            self.direction = 0
        # going right or left
        elif initial_direction == 1 or initial_direction == 3:
            position_x += 1
        # going down
        elif initial_direction == 2:
            position_y -= 1
            self.direction = 2
        else:
            raise NotImplementedError
        return position_x, position_y

    def _move_left(self, initial_direction, position_x, position_y):
        # going down
        if initial_direction == 2:
            position_y -= 1
            self.direction = 2
        # going right or left
        elif initial_direction == 1 or initial_direction == 3:
            position_x -= 1
        elif initial_direction == 0:
            position_y += 1
            self.direction = 0
        else:
            raise NotImplementedError
        return position_x, position_y

    def _move_up(self, initial_direction, position_x, position_y):
        if initial_direction == 3:
            position_x -= 1
            self.direction = 3
        elif initial_direction == 0 or initial_direction == 2:
            position_y += 1
        elif initial_direction == 1:
            position_x += 1
            self.direction = 1
        else:
            raise NotImplementedError
        return position_x, position_y

    def _move_down(self, initial_direction, position_x, position_y):
        if initial_direction == 1:
            position_x += 1
            self.direction = 1
        elif initial_direction == 0 or initial_direction == 2:
            position_y -= 1
        elif initial_direction == 3:
            position_x -= 1
            self.direction = 3
        else:
            raise NotImplementedError
        return position_x, position_y

    def position_is_out_of_map(self, position_x, position_y):
        return position_x == self.map_size or position_y == self.map_size or position_x < 0 or position_y < 0

    def move_to_the_other_side_of_the_map(self, position_x, position_y):
        new_position_x = position_x
        new_position_y = position_y

        if position_x == self.map_size:
            new_position_x = 0
        if position_x < 0:
            new_position_x = self.map_size - 1
        if position_y == self.map_size:
            new_position_y = 0
        if position_y < 0:
            new_position_y = self.map_size - 1

        return new_position_x, new_position_y

    def _create_observation(self):
        """
        This function creates a grayscale observation (image) from the current state of the game.
        :return:
        """
        # init map
        observations_ = np.zeros((self.map_size, self.map_size, 1))

        # add objects
        for collectible in self.collectables:
            observations_[collectible[0], collectible[1], 0] = 0.25
        # add pacman body
        observations_[self.body[-1][0], self.body[-1][1], 0] = 0.8

        return observations_

    def reset(self):
        self.body = []
        self.collectables = []
        self.direction = 1
        self.size = 1
        self.steps_ = 0
        self.last_observation = None

        self._create_body()
        self._create_collectables(num=10)
        observations_ = self._create_observation()
        return observations_.flatten()

    def render(self):
        """
        This function creates a cv2 plot from the current game state
        :param mode: not used, legacy of gym environments
        :return:
        """

        if self.last_observation is not None:
            image = np.float32(self.last_observation)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            # rescale original image from the grid world to visualize with OpenCv
            for i in range(self.displayed_img_size):
                for j in range(self.displayed_img_size):
                    self.displayed_img[i][j] = \
                        image[i // self.image_to_map_size_ratio][j // self.image_to_map_size_ratio]
            cv2.imshow("Pacman Env", self.displayed_img)
            # add wait to see the game
            cv2.waitKey(50)

    def _create_body(self):
        self.body.append((0, 0))
        self.size = 1

    def _create_collectables(self, num):
        for _ in range(num):
            coordinates = tuple(np.random.randint(0, self.map_size, (2,)))
            while coordinates in self.collectables or coordinates in self.body:
                coordinates = tuple(np.random.randint(0, self.map_size, (2,)))
            self.collectables.append(coordinates)

    def keyboard_on_press(self, key):
        try:
            if key.name == self.KEY_NAME_UP:
                self.direction = self.DIRECTION_UP
            elif key.name == self.KEY_NAME_DOWN:
                self.direction = self.KEY_NAME_DOWN
            elif key.name == self.KEY_NAME_RIGHT:
                self.direction = self.DIRECTION_RIGHT
            elif key.name == self.KEY_NAME_LEFT:
                self.direction = self.DIRECTION_LEFT
        except:
            return


if __name__ == "__main__":
    env = Pacman(map_size=10)
    listener = keyboard.Listener(on_press=env.keyboard_on_press)
    listener.start()
    done_ = False
    state = env.reset()
    steps_done = 0
    while not done_:
        state, reward, done_ = env.step(direction=env.direction)
        env.render()
        time.sleep(1)
        steps_done += 1
        if steps_done > 100:
            done_ = True
