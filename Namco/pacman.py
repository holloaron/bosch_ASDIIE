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

    def movement(self,action,x_pos,y_pos):
        # going up
        if action == 'w':
            pos_x -= 1
        # going left
        elif action == 'a':
            pos_y -= 1
        # going down
        elif action == 's':
            pos_x += 1
        # going right
        elif action == 'd':

        else:
            raise NotImplementedError
        return pos_x, pos_y



if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100)

    done_ = False
    while not done_:
        done_ = env.step()


