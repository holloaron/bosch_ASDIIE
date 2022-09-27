import numpy as np


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

    def step(self):
        done = False

        # Increasing the timestep
        self.time_step += 1

        # Terminating after max time steps
        if self.time_step > self.max_time_step:
            done = True

        return done

    def render(self):
        pass

    def movement(self,action,vel_x,vel_y):
        # going up
        if action == 'w':
            vel_x = -1
            vel_y = 0
        # going left
        elif action == 'a':
            vel_x = 0
            vel_y = -1
        # going down
        elif action == 's':
            vel_x = 1
            vel_y = 0
        # going right
        elif action == 'd':
            vel_x = 0
            vel_y = 1

        return vel_x, vel_y



if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100)

    done_ = False
    while not done_:
        done_ = env.step()


