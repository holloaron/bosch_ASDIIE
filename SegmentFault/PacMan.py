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
from Direction import Direction
import cv2
import numpy as np
import time
from threading import Thread
import os
from TimerThread import *
from MapData import MapData, MapElements
from Commands import *
from Player import *

class PacMan:
    movement_command = Commands.Nothing
    stop=False

    def __init__(self):
        self.Stopper = TimeCounter()
        self.Stopper.start()

        # load mapdata
        self.mapdata = MapData("Map.dat")
        
        # init Player
        self.player = Player(self.mapdata.get_first_coord_of(MapElements.PacMan), Direction.Down)
        
        self.step_ = 0
        self.last_obs = None

        map_size_multiplier=10
        self.map_size = self.mapdata.height
        self.show_img_size = (self.map_size * map_size_multiplier)
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.reset()


    def choose_next_action(self):
        while not self.stop:
            user_input=command_parser(input("Choose your next action:\n"))
            
            if is_movement_command(user_input):
                self.movement_command = user_input

            if user_input == Commands.Restart:
                self.reset()

            if user_input == Commands.Exit:
                self.Clean_up_and_close()
        

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
        timeout = 60
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
        state, reward, time_is_up = self.step()
        self.render()
        time.sleep(0.001)

    def step(self):
        self.player.score = 0
        self.player.is_dead = False
        x, y = self.calculate_new_position()
        self.player.score = self.checking_for_object_to_eat(self.player.score, x, y)
        obs = self.repaint_map()
        self.step_ += 1
        if self.step_ > 100:
            self.player.is_dead = True

        return obs.flatten(), self.player.score, self.player.is_dead

    def repaint_map(self):
        obs = self.create_observation()
        self.last_obs = obs
        return obs

    def calculate_new_position(self):
        poz_x = self.player.position[0]
        poz_y = self.player.position[1]
        x, y = self.set_new_position(self.movement_command, poz_x, poz_y)
        x, y = self.check_if_player_reached_the_border_of_the_map(x, y)
        self.player.position = (x, y)

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

        return x, y


    def set_new_position(self, command: Commands, pos_x, pos_y):
        if command == Commands.SetDirection_Right:
            return self.going_right(command, pos_x, pos_y)

        elif command == Commands.SetDirection_Down:
            return self.going_down(command, pos_x, pos_y)

        elif command == Commands.SetDirection_Left:
            return self.going_left(command, pos_x, pos_y)

        elif command == Commands.SetDirection_Up:
            return self.going_up(command, pos_x, pos_y)
        else:
            return (self.player.position)


    def going_right(self, action, pos_x, pos_y):
        # going up
        if action == Commands.SetDirection_Up:
            pos_y += 1
        # going right or left
        elif action == Commands.SetDirection_Right or action == Commands.SetDirection_Left:
            pos_x += 1
        # going down
        elif action == Commands.SetDirection_Down:
            pos_y -= 1

        return pos_x, pos_y

    def going_left(self, action, pos_x, pos_y):
        # going down
        if action == Commands.SetDirection_Down:
            pos_y -= 1
        # going right or left
        elif action == Commands.SetDirection_Right or action == Commands.SetDirection_Left:
            pos_x -= 1
        #going up
        elif action == Commands.SetDirection_Up:
            pos_y += 1

        return pos_x, pos_y

    def going_up(self, action, pos_x, pos_y):
        # going left
        if action == Commands.SetDirection_Left:
            pos_x -= 1
        # going up or down
        elif action == Commands.SetDirection_Up or action == Commands.SetDirection_Down:
            pos_y += 1
        # going right
        elif action == Commands.SetDirection_Right:
            pos_x += 1

        return pos_x, pos_y


    def going_down(self, action, pos_x, pos_y):
        # going right
        if action == Commands.SetDirection_Right:
            pos_x += 1
        # going up or down
        elif action == Commands.SetDirection_Up or action == Commands.SetDirection_Down:
            pos_y -= 1
        # going left
        elif action == Commands.SetDirection_Left:
            pos_x -= 1

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
        obs_[self.player.position[0], self.player.position[1], 0] = 1

        # walls
        for coord in self.walls:#self.mapdata.obstacles.walls:
            obs_[coord[0], coord[1], 0] = 0.45
        
        # points
        for coord in self.points:#self.mapdata.collectables.points:
            obs_[coord[0], coord[1], 0] = 0.25

        return obs_


    def reset(self):
        # stop PacMan
        self.movement_command = Commands.Nothing

        # reset MapData
        self.mapdata = MapData("Map.dat")

        # reset Player
        self.player.position = self.mapdata.get_first_coord_of(MapElements.PacMan)
        self.player.direction = Direction.Down

        
        self.objects = []
        self.step_ = 0
        self.last_obs = None

        self.walls = [] #self.mapdata.obstacles.walls
        self.points = []#self.mapdata.collectables.points
        self.coins = [] #self.mapdata.collectables.coins

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