
import cv2
import numpy as np
from typing import Tuple


class Pacman:
    def __init__(self, world_size: int, max_steps: int, show_window_size: int) -> None:
        """
        This function initializes the base attributes of the Pacman class
        :param world_size: size of the map
        :param max_steps: maximum amount of steps during the game
        :param show_window_size: size of the image in pixels
        """
        self.world_size = world_size
        self.max_steps = max_steps
        self.show_window_size = show_window_size
        # map components list
        self.body = []
        self.walls = []
        self.ghosts = []
        self.pellets = []
        # default values
        self.step_counter = 0
        self.direction = 1
        self.score = 0
        self.num_pellets = 10
        self.last_state = None
        # variables for world
        self.show_window = np.zeros((self.show_window_size, self.show_window_size, 3))
        self.ratio = int(self.show_window_size / self.world_size)
        self.reset()

    def step(self, action: int) -> Tuple[np.ndarray, int, bool, None]:
        """
        This function makes the steps in time during the game.
        :param action: chosen action by the user between 0-3, which refer to directions
        :return:
            obs (ndarray): observation from the current state of the game
            score (int): the points collected
            done (bool): tells whether the game is terminated or not
            info (str): additional information
        """
        pos_x, pos_y = self.body
        x, y = self._move(pos_x, pos_y, action)
        if (x, y) not in self.body:
            self.body = (x, y)

        obs = self._create_observation()
        self.last_state = obs

        self.score = self._check_pellets(x, y, self.score)

        self.step_counter += 1

        done = self.is_done(self.max_steps)

        info = None

        return obs.flatten(), self.score, done, info

    def is_done(self, max_steps: int) -> bool:
        """
        This function checks if the game has reached the maximum amount of timesteps.
        :param max_steps: maximum amount of steps during the game
        :return: boolean value
        """
        if self.step_counter > max_steps:
            print("Maximum time reached")
            return True
        else:
            return False

    def create_pacman(self) -> None:
        """
        This function creates Pacman and sets its starting position.
        :return: None
        """
        self.body = (0, 0)

    def create_pellets(self, numbers: int) -> None:
        """
        This function creates the pellets for Pacman to eat in the available positions of the map.
        :param numbers: the number of pellets to create
        :return: None
        """
        for _ in range(numbers):
            coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            while coordinates in self.pellets or coordinates in self.body:
                coordinates = tuple(np.random.randint(0, self.world_size, (2,)))
            self.pellets.append(coordinates)

    def _move(self, pos_x: int, pos_y: int, action: int) -> Tuple[int, int]:
        """
        This function is responsible for the movement of Pacman.
        :param pos_x: horizontal coordinate
        :param pos_y: vertical coordinate
        :param action: chosen action by the user between 0-3, which refer to directions
        :return: x, y (int): the new position of Pacman after the move was made.
        """
        self.direction = self._change_direction(action)
        if self.direction == 0:
            x, y = self._up(pos_x, pos_y)
        elif self.direction == 1:
            x, y = self._right(pos_x, pos_y)
        elif self.direction == 2:
            x, y = self._down(pos_x, pos_y)
        elif self.direction == 3:
            x, y = self._left(pos_x, pos_y)
        else:
            raise NotImplementedError
        return x, y

    @staticmethod
    def _change_direction(action: int) -> int:
        """
        This function changes the direction of Pacman according to the input action.
        :param action: chosen action by the user between 0-3, which refer to direction
        :return:
        """
        if 0 <= action < 4:
            direction = action
        else:
            raise ValueError("Please choose an action between 0-3")
        return direction

    def _up(self, pos_x: int, pos_y: int) -> Tuple[int, int]:
        """
        This function moves Pacman upwards.
        :param pos_x: vertical coordinate
        :param pos_y: horizontal coordinate
        :return: pos_x, pos_y (int): the updated coordinates
        """
        if pos_x - 1 < 0:
            pos_x = self.world_size
        else:
            pos_x -= 1
        return pos_x, pos_y

    def _right(self, pos_x: int, pos_y: int) -> Tuple[int, int]:
        """
        This function moves Pacman right.
        :param pos_x: vertical coordinate
        :param pos_y: horizontal coordinate
        :return: pos_x, pos_y (int): the updated coordinates
        """
        if pos_y + 1 == self.world_size:
            pos_y = 0
        else
            pos_y += 1
        return pos_x, pos_y

    def _down(self, pos_x: int, pos_y: int) -> Tuple[int, int]:
        """
        This function moves Pacman downwards.
        :param pos_x: vertical coordinate
        :param pos_y: horizontal coordinate
        :return: pos_x, pos_y (int): the updated coordinates
        """
        if pos_x + 1 == self.world_size:
            pos_x = 0
        else:
            pos_x += 1
        return pos_x, pos_y

    def _left(self, pos_x: int, pos_y: int) -> Tuple[int, int]:
        """
        This function moves Pacman left
        :param pos_x: vertical coordinate
        :param pos_y: horizontal coordinate
        :return: pos_x, pos_y (int): the updated coordinates
        """
        if pos_y - 1 < 0:
            pos_y = self.world_size - 1
        else:
            pos_y -= 1
        return pos_x, pos_y

    def _check_pellets(self, x: int, y: int, score: int) -> int:
        """
        This function checks if Pacman has interacted with a pellet.
        If so, the score increases and the pellet is removed from the map.
        :param x: horizontal coordinate
        :param y: vertical coordinate
        :return: None
        """
        if (x, y) in self.pellets:
            score += 1
            self.pellets.remove((x, y))
        return score

    def _create_observation(self) -> np.ndarray:
        """
        This function creates a grayscale observation from the current state of the game.
        :return: obs_ (ndarray): the created observation
        """
        obs_ = np.zeros((self.world_size, self.world_size, 1))
        # add pellets
        for pellet in self.pellets:
            obs_[pellet[0], pellet[1], 0] = 0.25
        # add Pacman
        body_coords = self.body
        obs_[body_coords[0], body_coords[1], 0] = 0.8
        return obs_

    def render(self) -> None:
        """
        This function is responsible for the visualization of the game.
        It creates a cv2 plot from the current game state.
        :return: None
        """
        if self.last_state is not None:
            img = np.float32(self.last_state)
        else:
            img = np.float32(self._create_observation())
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # rescale the image
        for i in range(self.show_window_size):
            for j in range(self.show_window_size):
                self.show_window[i][j] = img[i // self.ratio][j // self.ratio]
        cv2.imshow("Pacman", self.show_window)
        cv2.waitKey(50)

    def reset(self) -> np.ndarray:
        """
        This function restarts the game by restoring the initial values and creating a new session.
        :return: obs_ (ndarray): observation of the current state
        """
        self.body = []
        self.pellets = []
        self.step_counter = 0
        self.direction = 0
        self.score = 0
        self.num_pellets = 10
        self.last_state = None

        self.create_pacman()
        self.create_pellets(self.num_pellets)
        obs_ = self._create_observation()

        return obs_.flatten()


if __name__ == "__main__":
    env = Pacman(world_size=10, max_steps=200, show_window_size=300)
    done = False
    state = env.reset()
    while not done:
        env.render()
        a = int(input("Choose your next action:\n"))
        state, reward, done, info = env.step(action=a)
        print(f"Your score: {env.score}")
    print("Game over")
    print(f"Final score: {env.score}")
