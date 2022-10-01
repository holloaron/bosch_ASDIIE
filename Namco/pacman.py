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
        self.pacman = [0, 0]
        self.score = 0

    def reset(self):
        """
        Resets the environment
        :return: Current state of the map
        """
        # Generating the initial position of Pacman
        self.pacman[0] = np.random.randint(0, self.map_size)
        self.pacman[1] = np.random.randint(0, self.map_size)

        # Generating object positions
        self.generate_objects()

        # Creating observation
        observation = self.create_observation()

        return observation

    def step(self, action):
        """
        Steps the environment into its next state
        :param action: current user input (w, a ,s or d)
        :return: current state of the map, current score, terminating flag
        """
        terminate = False

        # Increasing the timestep
        self.time_step_cnt += 1

        # Moving pacman based on current action
        self.move_pacman(action)

        # Check whether Pacman moved on an object
        self.check_objects()

        # Creating observation
        observation = self.create_observation()

        # Terminating after max time steps
        if self.time_step_cnt > self.max_time_step:
            terminate = True

        return observation, self.score, terminate

    def render(self, observation):
        """
        Prints the current state of the environment on the console
        :param observation: Current state of the map
        :return: -
        """
        # Clearing console before printing the map (cannot clear the console in PyCharm, only in terminal)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Converting numpy array to python list
        observation = observation.tolist()

        # Replacing number with characters for visualization
        for x in range(self.map_size):
            for y in range(self.map_size):
                if observation[x][y] == EMPTY:
                    observation[x][y] = '-'
                elif observation[x][y] == PACMAN:
                    observation[x][y] = '0'
                elif observation[x][y] == OBJECT:
                    observation[x][y] = 'o'

        # Printing the current score and the current observation line by line with separation
        for line in observation:
            print(*line, sep='  ')

        print("\nCurrent score:", self.score)

    def create_observation(self):
        """
        Processes the positions of Pacman and the objects and creates the current state matrix
        :return: Current state of the map
        """
        # Creating the map
        observation = np.zeros((self.map_size, self.map_size), dtype=int)

        # Placing Pacman on the map
        observation[self.pacman[0], self.pacman[1]] = PACMAN

        # Placing the objects on the map
        for obj in self.objects:
            observation[obj[0], obj[1]] = OBJECT

        return observation

    def move_pacman(self, action):
        """
        Moves Pacman in the desired direction
        :param action: current user input (w, a, s or d)
        :return: -
        """
        # Moving up
        if action == 'w':
            self.pacman[0] = max(self.pacman[0] - 1, 0)
        # Moving left
        elif action == 'a':
            self.pacman[1] = max(self.pacman[1] - 1, 0)
        # Moving down
        elif action == 's':
            self.pacman[0] = min(self.pacman[0] + 1, self.map_size - 1)
        # Moving right
        elif action == 'd':
            self.pacman[1] = min(self.pacman[1] + 1, self.map_size - 1)

    def generate_objects(self):
        """
        Generates the given number of random objects on the map
        :return: -
        """
        for _ in range(self.num_of_objects):
            obj_coords = tuple(np.random.randint(0, self.map_size, (2,)))

            # Making sure that generated objects do not have the same position with each other or with Pacman
            while (obj_coords in self.objects) or (obj_coords in tuple(self.pacman)):
                obj_coords = tuple(np.random.randint(0, self.map_size, (2,)))

            self.objects.append(obj_coords)

    def check_objects(self):
        """
        Checks whether Pacman picked up an object and increases the score accordingly
        :return: -
        """
        for obj in self.objects:
            if obj == tuple(self.pacman):
                # If Pacman moved on an object, increase the score and remove the object
                self.score += 1
                self.objects.remove(obj)


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



