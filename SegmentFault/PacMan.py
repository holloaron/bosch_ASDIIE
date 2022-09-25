"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : PacMan.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
(...)

********************************************************************
********************************************************************
"""
import cv2
import numpy as np
import time
from threading import Thread
import os
from TimerThread import *
from MapData import *
#from ActionParser import *


class PacMan:
    direction_command = '0'
    stop=False
    old_direction_command = '0'

    class Direction(Enum):
        Up = 0
        Right = 1
        Down = 2
        Left = 3


    def __init__(self):
        self.start_stopper()
        self.create_mapdata()
        self.create_lists_for_the_map_contents()
        self.set_default_values()
        self.set_visualisation()

    def set_visualisation(self):
        map_size_multiplier=10
        self.show_img_size = (self.map_size * map_size_multiplier)
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.reset()

    def set_default_values(self):
        self.step_ = 0
        self.direction = 1
        self.last_obs = None

    def create_lists_for_the_map_contents(self):
        self.body = (0, 0)
        self.objects = []
        self.walls = []
        self.points = []

    def start_stopper(self):
        self.Stopper = TimeCounter()
        self.Stopper.start()

    def create_mapdata(self):
        self.mapdata = MapData("Map.dat")
        self.set_map_data()
        print(self.map_size)

    def set_map_data(self):
        self.map_height = self.mapdata.height
        self.map_width = self.mapdata.width
        self.map_size = self.map_height
        if self.map_height < self.map_width:
            self.map_size = self.map_width

    def choose_next_action(self):
        while not self.stop:
            self.get_next_direction()
        print('stopped')

    def get_next_direction(self):
        user_input=input("Choose your next action:\n")
        if self.is_integer(user_input):
            self.direction_command = user_input
        else:
            pass

    def auto_step(self):
        global state, reward, time_is_up
        start_time, step_time, timeout = self.time_init()
        while not time_is_up:
            start_time = self.execute_step(start_time, step_time)
            time_is_up = self.timeout(timeout)
        if time_is_up:
            self.Clean_up_and_close()

    def time_init(self)->tuple:
        step_time = 0.5
        timeout = 10
        start_time = time.time()
        return start_time, step_time, timeout

    def execute_step(self, start_time: float , step_time:float)->float:
        time_taken = time.time() - start_time
        if time_taken > step_time:
            self.render_step()
            start_time = time.time()

        return start_time

    def render_step(self):
        global state, reward, time_is_up
        state, reward, time_is_up = self.step(action=self.direction_command)
        self.render()
        time.sleep(0.001)

    def step(self, action:str):
        score = 0
        is_dead = False
        x, y = self.calculate_new_position(action)
        score = self.checking_for_object_to_eat(score, x, y)
        obs = self.repaint_map()
        self.step_ += 1
        if self.step_ > 100:
            is_dead = True

        return obs.flatten(), score, is_dead

    def repaint_map(self):
        obs = self.create_observation()
        self.last_obs = obs
        return obs

    def calculate_new_position(self, action):
        pos_x, pos_y = self.get_current_position()
        if len(action) == 1:
            action = int(action)
            x, y = self.set_new_position(action, pos_x, pos_y)
        x, y = self.check_if_player_reached_the_border_of_the_map(x, y)

        return x, y

    def checking_for_object_to_eat(self, score, x, y):
        # checking for object to eat
        if (x, y) in self.objects:
            score = 1
            self.objects.remove((x, y))
            # self._create_objects(num=1) # use this line for generating new object if one is eaten

        return score

    def check_if_player_reached_the_border_of_the_map(self, x, y):
        # check if the player reached the end of the map
        x = self.check_borders(x)
        y = self.check_borders(y)
        self.body = (x, y)

        return x, y

    def get_current_position(self):
        pos_x = self.body[0]
        pos_y = self.body[1]

        return pos_x, pos_y

    def set_new_position(self, action, pos_x, pos_y):
        if self.direction == 0:
            x, y, = self.going_up(action, pos_x, pos_y)
        elif self.direction == 1:
            x, y, = self.going_right(action, pos_x, pos_y)
        elif self.direction == 2:
            x, y, = self.going_down(action, pos_x, pos_y)
        elif self.direction == 3:
            x, y, = self.going_left(action, pos_x, pos_y)
        else:
            raise NotImplementedError

        return x, y

    def is_integer(self,string:str):
        try:
            float(string)
        except ValueError:

            return False
        else:

            return True


    def going_right(self, action, pos_x, pos_y):
        # going up
        if action == 0:
            pos_y += 1
            self.direction = 0
        # going right or left
        elif action == 1 or action == 3:
            pos_x += 1
        # going down
        elif action == 2:
            pos_y -= 1
            self.direction = 2
        else:
            raise NotImplementedError

        return pos_x, pos_y

    def going_left(self, action, pos_x, pos_y):
        # going down
        if action == 2:
            pos_y -= 1
            self.direction = 2
        # going right or left
        elif action == 1 or action == 3:
            pos_x -= 1
        #going up
        elif action == 0:
            pos_y += 1
            self.direction = 0
        else:
            raise NotImplementedError

        return pos_x, pos_y

    def going_up(self, action, pos_x, pos_y):
        # going left
        if action == 3:
            pos_x -= 1
            self.direction = 3
        # going up or down
        elif action == 0 or action == 2:
            pos_y += 1
        # going right
        elif action == 1:
            pos_x += 1
            self.direction = 1
        else:
            raise NotImplementedError
        return pos_x, pos_y


    def going_down(self, action, pos_x, pos_y):
        # going right
        if action == 1:
            pos_x += 1
            self.direction = 1
        # going up or down
        elif action == 0 or action == 2:
            pos_y -= 1
        # going left
        elif action == 3:
            pos_x -= 1
            self.direction = 3
        else:
            raise NotImplementedError
        return pos_x, pos_y


    def check_borders(self, coord):
        # checking the limit at max
        if coord == self.map_size:
            return 0
        # checking limit at min
        elif coord < 0:
            return self.map_size - 1
        # state is in boundaries
        else:
            return coord


    def create_observation(self):
        """
        This funtcion creates a grayscale observation (image) from the current state of the game.
        :return:
        """
        # init map
        obs_ = np.zeros((self.map_size, self.map_size, 1))

        # add objects
        for obj in self.objects:
            obs_[obj[0], obj[1], 0] = 0.25
        
        # add player
        obs_[self.body[0], self.body[1], 0] = 1

        # walls
        for obj in self.walls:
            obs_[obj[0], obj[1], 0] = 0.45
        
        # points
        for obj in self.points:
            obs_[obj[0], obj[1], 0] = 0.25

        return obs_


    def reset(self):
        self.body = self.mapdata.get_first_coord_of(MapElements.PacMan)
        self.objects = []
        self.direction = 1
        self.step_ = 0
        self.last_obs = None

        #self.walls = self.mapdata.get_coords_of(MapElements.Wall)
        self.points = self.mapdata.get_coords_of(MapElements.Point)

        obs_ = self.create_observation()
        return obs_.flatten()


    def render(self, mode="human"):
        """
        This function creates a cv2 plot from the current game state
        :param mode: not used, legacy of gym environments
        :return:
        """

        if self.last_obs is not None:
            img = np.float32(self.last_obs)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            # rescale original image from the grid world to visualize with OpenCv
            for i in range(self.show_img_size):
                for j in range(self.show_img_size):
                    self.show_img[i][j] = img[i // self.ratio][j // self.ratio]
            cv2.imshow("PacMan", self.show_img)
            # add wait to see the game
            cv2.waitKey(50)


    def timeout(self, timelimit):
        if self.Stopper.seconds_passed >= timelimit:
            print(f"You have reached the:  {timelimit} s time limit")
            return True
        else:
            False

    def Clean_up_and_close(self):
        os._exit(0)



if __name__ == "__main__":
    env = PacMan()
    time_is_up = False
    state = env.reset()
    t1 = Thread(target=env.choose_next_action)
    t2 = Thread(target=env.auto_step)
    t1.start()
    t2.start()
    t2.join()
    env.stop = True