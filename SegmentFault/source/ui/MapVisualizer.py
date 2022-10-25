"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapVisualizer.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module for map rendering

/*********************************************************************
/*********************************************************************
"""
import cv2
import numpy as np
from Player import Player
from MapData import MapData

class MapVisualizer:
    def __init__(self, mapdata: MapData, ratio: int = 10) -> None:
        self.ratio = ratio
        self.height = mapdata.height * self.ratio
        self.width = mapdata.width * self.ratio
        self.size = np.zeros((self.height, self.width, 3))

        self.grayscale = GrayScale(mapdata)

class GrayScale:
    def __init__(self, mapdata: MapData, visualdata: MapVisualizer) -> None:
        self.mapdata = mapdata
        self.visualdata = visualdata
        self.game_state = None
        self.rendered_image = None

        # color values
        self.player_color = 1
        self.ghost_color = 0.75
        self.door_color = 0.55
        self.wall_color = 0.45
        self.point_color = 0.25
        self.coin_color = 0.35

    def refresh_state(self, player: Player) -> any:
        """ Creates a matrix with the current game state

        @args:

        @return:

        """
        self.matrix = np.zeros((self.mapdata.height, self.mapdata.width, 1))

        # add player
        self.matrix[player.position[0], player.position[1], 0] = self.player_color

        # add obstacles
        # walls
        for coord in self.mapdata.obstacles.walls:
            self.matrix[coord[0], coord[1], 0] = self.wall_color
        
        # door
        self.matrix[self.mapdata.obstacles.door[0], self.mapdata.obstacles.door[1], 0] = self.door_color

        # add collectables
        # points
        for coord in self.mapdata.collectables.points:
            self.matrix[coord[0], coord[1], 0] = self.point_color
        
        # coins
        for coord in self.mapdata.collectables.coins:
            self.matrix[coord[0], coord[1], 0] = self.coin_color

        # add enemies

    def render_game_state(self, mode = "human"):
        """
        """
        if self.game_state is not None:
            image = np.float32(self.matrix)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            # rescale original image from the grid world to visualize with OpenCv
            for height in range(self.visualdata.height):
                for width in range(self.visualdata.width):
                    self.rendered_image[height][width] = image[height // self.visualdata.ratio][width // self.visualdata.ratio]
            
            # show window
            cv2.imshow("PacMan", self.rendered_image)

            # add wait to see the game
            cv2.waitKey(50)

