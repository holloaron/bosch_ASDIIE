import numpy as np

# Constants
PACMAN = 1
OBJECT = 2


class PacMan:
    def __init__(self, map_size=10, max_time_step=100):
        # PacMan variables
        self.map_size = map_size
        self.time_step_cnt = 0
        self.max_time_step = max_time_step
        self.x = np.random.randint(0, self.map_size)
        self.y = np.random.randint(0, self.map_size)
        self.objects = []
        self.score = 0

    def reset(self):
        pass

    def step(self, action):
        terminate = False

        # Increasing the timestep
        self.time_step_cnt += 1

        # Moving pacman based on current action
        self.move_pacman(action)

        observation = self.create_observation()

        # Terminating after max time steps
        if self.time_step_cnt > self.max_time_step:
            terminate = True

        return observation, self.score, terminate

    def render(self, observation):
        print(observation)

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


if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100)
    # Reset environment
    env.reset()

    done = False

    while not done:
        user_input = input("Select your next action (W, A, S, D): ")
        state, reward, done = env.step(user_input)
        env.render(state)



