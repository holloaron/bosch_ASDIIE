"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : GrayScaleVisualizer.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module for rendering grayscale map

/*********************************************************************
/*********************************************************************
"""
import cv2
import numpy as np
from source.map import MapData

class GrayScaleVisualizer():
    def __init__(self, mapdata: MapData) -> None:
        self.mapdata = mapdata
        self.ratio = 10
        self.height = mapdata.height * self.ratio
        self.width = mapdata.width * self.ratio

        self.game_state = None
        self.rendered_image = None

        # color values
        self.player_color = 1
        self.ghost_color = 0.75
        self.door_color = 0.55
        self.wall_color = 0.45
        self.point_color = 0.25
        self.coin_color = 0.35

    def refresh_game_state(self):
        """ Creates a matrix with the current game state
        """
        self.game_state = np.zeros((self.mapdata.height, self.mapdata.width, 1))

        # add player
        self.game_state[self.mapdata.Player[0], self.mapdata.Player[1], 0] = self.player_color

        # add obstacles
        # walls
        for coord in self.mapdata.obstacles.walls:
            self.game_state[coord[0], coord[1], 0] = self.wall_color
        
        # door
        self.game_state[self.mapdata.obstacles.door[0], self.mapdata.obstacles.door[1], 0] = self.door_color

        # add collectables
        # points
        for coord in self.mapdata.collectables.points:
            self.game_state[coord[0], coord[1], 0] = self.point_color
        
        # coins
        for coord in self.mapdata.collectables.coins:
            self.game_state[coord[0], coord[1], 0] = self.coin_color

        #TODO: add enemies


    def render_game_state(self):
        """
        """
        if self.game_state is not None:
            image = np.float32(self.game_state)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            # rescale original image from the grid world to visualize with OpenCv
            for height in range(self.height):
                for width in range(self.width):
                    self.rendered_image[height][width] = image[height // self.ratio][width // self.ratio]
            
            # show window
            cv2.imshow("PacMan", self.rendered_image)

            # add wait to see the game
            cv2.waitKey(50)