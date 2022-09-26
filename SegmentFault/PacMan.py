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
    def __init__(self):
        self.movement_command = Commands.Nothing
        self.stop = False

        self.Stopper = TimeCounter()
        self.Stopper.start()

        # load mapdata
        self.mapdata = MapData("Map.dat")
        
        # init Player
        self.player = Player(self.mapdata.get_first_coord_of(MapElements.PacMan), Direction.Down)
        
        self.step_ = 0
        self.last_obs = None

        self.map_ratio = 10
        self.shown_map_height = self.mapdata.height * self.map_ratio
        self.shown_map_width = self.mapdata.width * self.map_ratio
        self.show_img = np.zeros((self.shown_map_height, self.shown_map_width, 3))

        self.reset()


    def choose_next_action(self):
        """ 
        """
        while not self.stop:
            user_input=command_parser(input("Choose your next action:\n"))
            
            if is_movement_command(user_input):
                self.movement_command = user_input

            if user_input == Commands.Restart:
                self.reset()

            if user_input == Commands.Exit:
                self.Clean_up_and_close()
        

    def auto_step(self):
        """
        """
        global state, reward, time_is_up

        # init parameters
        start_time = time.time()
        time_step = 0.5
        timeout = 60

        while not time_is_up:

            time_taken = time.time() - start_time

            if time_taken > time_step:
                state, reward, time_is_up = self.step()
                self.render()
                time.sleep(0.001)
                start_time = time.time()

            time_is_up = self.is_timeout(timeout)

        self.Clean_up_and_close()


    def step(self) -> tuple[any, int, bool]:
        """
        """
        self.player.position = self.calculate_new_position(self.movement_command, self.player.position[0], self.player.position[1])
        self.player.score += self.check_collectables(self.player.position[0], self.player.position[1])

        obs = self.create_observation()
        self.last_obs = obs

        self.step_ += 1
        if self.step_ > 100:
            self.player.is_dead = True

        return obs.flatten(), self.player.score, self.player.is_dead

    def calculate_new_position(self, command: Commands, pos_x: int, pos_y: int) -> tuple[int, int]:
        """ Calculates the next position depemding on the given command
        
        @args:

        @return:

        """
        if command == Commands.SetDirection_Right:
            self.player.direction = Direction.Right
            pos_y += 1

        if command == Commands.SetDirection_Down:
            self.player.direction = Direction.Down
            pos_x += 1

        if command == Commands.SetDirection_Left:
            self.player.direction = Direction.Left
            pos_y -= 1

        if command == Commands.SetDirection_Up:
            self.player.direction = Direction.Up
            pos_x -= 1
        
        pos_x, pos_y = self.check_obstacles(pos_x, pos_y)
        pos_x, pos_y = self.check_borders(pos_x, pos_y)

        return (pos_x, pos_y)


    def check_obstacles(self, pos_x: int, pos_y: int):
        """ Checks if any obstacle is in front of the player
        
        @args:

        @returns:

        """
        obstacle_ahead = False

        # check walls
        if (pos_x, pos_y) in self.mapdata.obstacles.walls:
            obstacle_ahead = True
        
        # check door
        if (pos_x, pos_y) == self.mapdata.obstacles.door:
            obstacle_ahead = True

        if obstacle_ahead:

            # reset player position
            if self.player.direction == Direction.Right:
                pos_y -= 1
            if self.player.direction == Direction.Down:
                pos_x -= 1
            if self.player.direction == Direction.Left:
                pos_y += 1
            if self.player.direction == Direction.Up:
                pos_x += 1
            
            # stop autostep
            self.movement_command = Commands.Nothing

        return (pos_x, pos_y)


    def check_borders(self, pos_x: int, pos_y: int) -> tuple[int, int]:
        """ Checks is the player reached the end of the map
            on any direction
        
        @args:

        @return:

        """
        
        # check map bottom
        if pos_x == self.mapdata.height:
            pos_x = 0
        
        # check map top
        if pos_x < 0:
            pos_x = self.mapdata.height - 1
        
        # check map left
        if pos_y == self.mapdata.width:
            pos_y = 0

        # check map right
        if pos_y < 0:
            pos_y = self.mapdata.width - 1
        
        return (pos_x, pos_y)


    def check_collectables(self, pos_x: int, pos_y: int):

        # check for points
        if (pos_x, pos_y) in self.mapdata.collectables.points:
            self.mapdata.collectables.points.remove((pos_x, pos_y))
            return 10

        # check for coins
        if (pos_x, pos_y) in self.mapdata.collectables.coins:
            self.mapdata.collectables.coins.remove((pos_x, pos_y))
            return 20

        # check for cherry (cherry is not implemented yet)


        return 0


    def create_observation(self):
        """
        This funtcion creates a grayscale observation (image) from the current state of the game.
        :return:
        """
        # init map
        obs_ = np.zeros((self.mapdata.height, self.mapdata.width, 1))

        # add objects
        for obj in self.objects:
            obs_[obj[0], obj[1], 0] = 0.25
        
        # add player
        obs_[self.player.position[0], self.player.position[1], 0] = 1

        # walls
        for coord in self.mapdata.obstacles.walls:
            obs_[coord[0], coord[1], 0] = 0.45
        
        # points
        for coord in self.mapdata.collectables.points:
            obs_[coord[0], coord[1], 0] = 0.25

        # coins
        for coord in self.mapdata.collectables.coins:
            obs_[coord[0], coord[1], 0] = 0.35

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
            for height in range(self.shown_map_height):
                for width in range(self.shown_map_width):
                    self.show_img[height][width] = img[height // self.map_ratio][width // self.map_ratio]
            
            cv2.imshow("PacMan", self.show_img)

            # add wait to see the game
            cv2.waitKey(50)


    def is_timeout(self, timelimit: int) -> bool:
        """ 
        @args:
            timelimit [int] - the 
        """
        if self.Stopper.seconds_passed >= timelimit:
            print(f"You have reached the:  {timelimit} s time limit")
            return True
        else:
            False

    def Clean_up_and_close(self):
        """ Forces the program to shut down
        """
        os._exit(0)


# program entry point
if __name__ == "__main__":
    env = PacMan()
    time_is_up = False
    t1 = Thread(target=env.choose_next_action)
    t2 = Thread(target=env.auto_step)
    t1.start()
    t2.start()
    t2.join()
    env.stop = True