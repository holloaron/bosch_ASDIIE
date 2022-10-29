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
from turtle import right
from Direction import Direction
import cv2
import numpy as np
import time
from threading import Thread
import os

from source import Timer
from source.ui import Terminal
from source.commands import *

class PacMan:
    def __init__(self):
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


    def get_user_input(self) -> None:
        """ User interaction logic
        """
        while not self.stop:
            user_input=command_parser(input("Choose your next action:\n"))
            
            # CHANGE DIRECTION
            if is_movement_command(user_input):
                if user_input == Commands.SetDirection_Right:
                    self.player.next_direction = Direction.Right

                if user_input == Commands.SetDirection_Down:
                    self.player.next_direction = Direction.Down

                if user_input == Commands.SetDirection_Left:
                    self.player.next_direction = Direction.Left

                if user_input == Commands.SetDirection_Up:
                    self.player.next_direction = Direction.Up

            # RESET GAME
            if user_input == Commands.Restart:
                self.reset()

            # EXIT GAME
            if user_input == Commands.Exit:
                self.Clean_up_and_close()


    def auto_step(self) -> None:
        """ Autamate game state change
            Shuts down the game on a specific time limit
        """
        global state, reward, time_is_up

        # init timing parameters
        start_time = time.time()
        time_step = 0.5
        game_timeout = 60

        while not time_is_up:

            time_taken = time.time() - start_time

            if time_taken > time_step:
                state, reward, time_is_up = self.step()
                self.render()
                time.sleep(0.001)
                start_time = time.time()

            time_is_up = self.is_timeout(game_timeout)

        self.Clean_up_and_close()


    def is_timeout(self, timelimit: int) -> bool:
        """ Determines if the timelimit for the game is passed or not

        @args:
            timelimit [int] - the timelimit for the game
        @return:
            True, if the given timelimit in secunds is up
        """
        if self.Stopper.seconds_passed >= timelimit:
            print(f"You have reached the:  {timelimit} s time limit")
            return True
        else:
            False


    def step(self) -> tuple[any, int, bool]:
        """ Player-Map interaction
        """
        self.player.position = self.set_player_position(self.player.position[0], self.player.position[1])
        self.player.score += self.set_score(self.player.position[0], self.player.position[1])

        obs = self.create_observation()
        self.last_obs = obs

        self.step_ += 1
        if self.step_ > 100:
            self.player.is_dead = True

        return obs.flatten(), self.player.score, self.player.is_dead

    def set_player_position(self, pos_x: int, pos_y: int) -> tuple[int, int]:
        """ Sets the players new position based on the mapdata, current position and direction
        
        @args:
            (pos_x, pos_y) [int, int] - the player current position
        @return:
            (pos_x, pos_y) [int, int] - the player new position
        """

        # change the direction, if turning is available
        if self.player.next_direction != None:
            test_x, test_y = self.next_position(self.player.next_direction, pos_x, pos_y)
            if not self.is_obstacle(test_x, test_y):
                self.player.direction = self.player.next_direction
                self.player.next_direction = None
        
        # calculate the next position
        pos_x, pos_y = self.next_position(self.player.direction, pos_x, pos_y)

        # reset position if obstacle ahead
        if self.is_obstacle(pos_x, pos_y):
            pos_x, pos_y = self.reset_position(self.player.direction, pos_x, pos_y)

        # jump to the other side
        pos_x, pos_y = self.check_borders(pos_x, pos_y)

        return (pos_x, pos_y)

    def is_obstacle(self, pos_x: int, pos_y: int) -> bool:
        """ Determines if there is an obstacle on the given coordinates or not

        @args:
            (pos_x, pos_y) [int, int] - position on the map
        @return:
            True, if ther is an obstacle on the given coordinates
        """

        # check walls
        if (pos_x, pos_y) in self.mapdata.obstacles.walls:
            return True
        
        # check door
        if (pos_x, pos_y) == self.mapdata.obstacles.door:
            return True
        
        return False

    def next_position(self, direction: Direction, pos_x: int, pos_y: int) -> tuple[int, int]:
        """ Gets the next position based on the current position and the direction

        @args:
            direction [Direction] - the direction of the movement
            (pos_x, pos_y) [int, int] - the current position
        @return:
            (pos_x, pos_y) [int, int] - the next position
        """
        if direction == Direction.Right:
            pos_y += 1
        if direction == Direction.Down:
            pos_x += 1
        if direction == Direction.Left:
            pos_y -= 1
        if direction == Direction.Up:
            pos_x -= 1
        
        return (pos_x, pos_y)


    def reset_position(self, direction: Direction, pos_x: int, pos_y: int):
        """ Resets the player position to the last position based on the direction
        
        @args:
            direction [Direction] - the direction of the movement
            (pos_x, pos_y) [int, int] - the player current position
        @return:
            (pos_x, pos_y) [int, int] - the player last position
        """
        if self.player.direction == Direction.Right:
            pos_y -= 1
        if self.player.direction == Direction.Down:
            pos_x -= 1
        if self.player.direction == Direction.Left:
            pos_y += 1
        if self.player.direction == Direction.Up:
            pos_x += 1
            
        return (pos_x, pos_y)

    def check_borders(self, pos_x: int, pos_y: int) -> tuple[int, int]:
        """ Checks is the player reached the end of the map
            on any direction
            If the player reaches the border, sets the player position
            to the other side of the map
        
        @args:
            (pos_x, pos_y) [int, int] - the player current position
        @return:
            (pos_x, pos_y) [int, int] - the player new position
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


    def set_score(self, pos_x: int, pos_y: int):
        """ Returns the score value of the given coordinate

        @args:
            (pos_x, pos_y) [int, int] - the player current position
        @return:
            score [int] - the value of the reward on the given coordinates
        """

        # check for points
        if (pos_x, pos_y) in self.mapdata.collectables.points:
            self.mapdata.collectables.points.remove((pos_x, pos_y))
            return 10

        # check for coins
        if (pos_x, pos_y) in self.mapdata.collectables.coins:
            self.mapdata.collectables.coins.remove((pos_x, pos_y))
            return 20

        #TODO: check for cherry

        #TODO: check for ghosts

        return 0


    def create_observation(self) -> any:
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


    def reset(self) -> any:
        # reset MapData
        self.mapdata = MapData("Map.dat")

        # reset Player
        self.player = Player(self.mapdata.get_first_coord_of(MapElements.PacMan), Direction.Down)


        self.objects = []
        self.step_ = 0
        self.last_obs = None

        obs_ = self.create_observation()
        return obs_.flatten()


    def render(self, mode="human") -> None:
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


    def Clean_up_and_close(self) -> None:
        """ Forces the program to shut down
        """
        os._exit(0)


# program entry point
if __name__ == "__main__":
    env = PacMan()
    time_is_up = False
    t1 = Thread(target=env.get_user_input)
    t2 = Thread(target=env.auto_step)
    t1.start()
    t2.start()
    t2.join()
    env.stop = True