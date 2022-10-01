import numpy as np
import os

# Constants
EMPTY = 0
PACMAN = 1
OBJECT = 2


class PacMan:
    def __init__(self, map_size=10, max_time_step=100, num_of_objects=10):
        # PacMan variables
        self.map_size = map_size
        self.time_step_cnt = 0
        self.max_time_step = max_time_step
        self.objects = []
        self.num_of_objects = num_of_objects
        self.x = 0
        self.y = 0
        self.score = 0

    def reset(self):
        # Generating the initial position of Pacman
        self.x = np.random.randint(0, self.map_size)
        self.y = np.random.randint(0, self.map_size)

        # Generating object positions
        self.generate_objects()

        # Creating observation
        observation = self.create_observation()

        return observation

    def step(self, action):
        terminate = False

        # Increasing the timestep
        self.time_step_cnt += 1

        # Moving pacman based on current action
        self.move_pacman(action)

        # Creating observation
        observation = self.create_observation()

        # Terminating after max time steps
        if self.time_step_cnt > self.max_time_step:
            terminate = True

        return observation, self.score, terminate

    def render(self, observation):
        # Clearing console before printing the map (cannot clear the console in PyCharm, only in terminal)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Converting numpy array to python list
        observation = observation.tolist()

        # Processing the observation for visualizing
        for x in range(self.map_size):
            for y in range(self.map_size):
                if observation[x][y] == EMPTY:
                    observation[x][y] = '-'
                elif observation[x][y] == PACMAN:
                    observation[x][y] = '0'
                elif observation[x][y] == OBJECT:
                    observation[x][y] = 'o'

        # Printing the current observation line by line with separation
        for line in observation:
            print(*line, sep='  ')

        print("\nCurrent score:", self.score)

    def create_observation(self):
        # Creating the map
        observation = np.zeros((self.map_size, self.map_size), dtype=int)

        observation[self.x, self.y] = PACMAN

        return observation

    def move_pacman(self, action):
        # Moving up
        if action == 'w':
            self.x = max(self.x - 1, 0)
        # Moving left
        elif action == 'a':
            self.y = max(self.y - 1, 0)
        # Moving down
        elif action == 's':
            self.x = min(self.x + 1, self.map_size - 1)
        # Moving right
        elif action == 'd':
            self.y = min(self.y + 1, self.map_size - 1)

    def generate_objects(self):
        pass


if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100,
                 num_of_objects=10)

    # Reset environment and render the initial state
    state = env.reset()
    env.render(state)

    done = False

    while not done:
        user_input = input("Select your next action (W, A, S, D): ")
        state, reward, done = env.step(user_input)
        env.render(state)



