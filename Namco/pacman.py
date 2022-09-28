import numpy as np
from pytimedinput import timedInput

class PacMan:
    def __init__(self, map_size=10, max_time_step=100):
        # PacMan variables
        self.map_size = map_size
        self.time_step = 0
        self.max_time_step = max_time_step
        self.map = np.zeros((map_size, map_size))
        self.x = np.random.randint(0, self.map_size)
        self.y = np.random.randint(0, self.map_size)

    def reset(self):
        pass

    def step(self, action):
        done = False

        # Increasing the timestep
        self.time_step += 1

        # Terminating after max time steps
        if self.time_step > self.max_time_step:
            done = True

        return done

    def render(self):
        pass

    # Selecting automatic action if no user input (direction) given
    def select_action(self, prev_action):
        user_input, timedOut = timedInput("Choose your next action:\n")
        if timedOut:
            action = prev_action
        else:
            action = user_input
            prev_action = user_input
        return prev_action, action

if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100)

    done_ = False
    # First step
    user_input = input("Choose your first action (Please enter WASD keys to move):\n")
    done = env.step(user_input)
    prev_action = user_input
    while not done_:
        action = env.select_action(prev_action)
        done_ = env.step(action)


