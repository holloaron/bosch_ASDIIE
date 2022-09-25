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

from TimerThread import *
from MapData import *
#from ActionParser import *


class PacMan:
    answer = ''
    stop=False
    old_answer = '0'

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
        self.show_img_size = (self.map_size * 10)
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

    def ask(self):
        # get the command from the consol
        #global state, reward, done_, info
        while not self.stop:
            self.answer = input("Choose your next action:\n")
            #time.sleep(0.001)
            self.old_answer = self.answer
            # state, reward, done_, info = self.step(action=self.old_answer)
            # self.render()


    def auto_step(self):
        # step the point at a given intervals
        global state, reward, done_, info
        time_limit = 0.5
        start_time = time.time()
        while not done_:
            time_taken = time.time() - start_time

            # print(f"The answer is {answer} .")

            if time_taken > time_limit:
                state, reward, done_, info = self.step(action=self.old_answer)
                self.render()
                time.sleep(0.001)
                start_time = time.time()

            done_ = self.timeout(60)


    def step(self, action):
        # setting base reward
        score = 0
        # setting basic env status
        is_dead = False

        # get the current position of the player
        pos_x = self.body[0]
        pos_y = self.body[1]

        if len(action) == 1:

            action = int(action)

            # get new player position
            if self.direction == 0:
                x, y, = self._going_up(action, pos_x, pos_y)
            elif self.direction == 1:
                x, y, = self._going_right(action, pos_x, pos_y)
            elif self.direction == 2:
                x, y, = self._going_down(action, pos_x, pos_y)
            elif self.direction == 3:
                x, y, = self._going_left(action, pos_x, pos_y)
            else:
                raise NotImplementedError
        
        else:
            pass

        # check if the player reached the end of the map
        x = self._check_borders(x)
        y = self._check_borders(y)

        self.body = (x, y)

        # checking for object to eat
        if (x, y) in self.objects:
            score = 1
            self.objects.remove((x, y))
            # self._create_objects(num=1) # use this line for generating new object if one is eaten

        # create observation
        obs = self._create_observation()

        # save observation
        self.last_obs = obs

        # placeholder for additional information
        info = None

        # count the steps of the game
        self.step_ += 1

        # terminating the game after some step
        if self.step_ > 100:
            is_dead = True

        return obs.flatten(), score, is_dead, info


    def _going_right(self, action, pos_x, pos_y):
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


    def _going_left(self, action, pos_x, pos_y):
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


    def _going_up(self, action, pos_x, pos_y):
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


    def _going_down(self, action, pos_x, pos_y):
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


    def _check_borders(self, coord):
        # checking the limit at max
        if coord == self.map_size:
            return 0
        # checking limit at min
        elif coord < 0:
            return self.map_size - 1
        # state is in boundaries
        else:
            return coord


    def _create_observation(self):
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

        obs_ = self._create_observation()
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



if __name__ == "__main__":
    env = PacMan()
    done_ = False
    state = env.reset()
    t1 = Thread(target=env.ask)
    t2 = Thread(target=env.auto_step)
    t1.start()
    t2.start()
    t2.join()
    env.stop = True
    print("program end")