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
Superclass for moving object in the game

********************************************************************
********************************************************************
"""

from Direction import Direction
from MapData import MapData


class Movable():
    def __init__(self,mapdata: MapData, start_position: tuple[int, int], start_direction: Direction) -> None:
        self.mapdata = mapdata
        self.position = start_position
        self.direction = start_direction
        self.next_direction = None
    
        
    def get_next_position(self) -> tuple[int, int]:
        """ Calculates the next position based on the current position and the direction

        @return:
            (pos_x, pos_y) [int, int] - the next position
        """
        pos_x = self.position[0]
        pos_y = self.position[1]

        if self.direction == Direction.Right:
            pos_y += 1
        if self.direction == Direction.Down:
            pos_x += 1
        if self.direction == Direction.Left:
            pos_y -= 1
        if self.direction == Direction.Up:
            pos_x -= 1
        
        return (pos_x, pos_y)

    
    def get_original_position(self) -> tuple[int, int]:
        """ Calculates the movalble object position original position based on thier direction
        
        @return:
            (pos_x, pos_y) [int, int] - the player last position
        """
        pos_x = self.position[0]
        pos_y = self.position[1]

        if self.direction == Direction.Right:
            pos_y -= 1
        if self.direction == Direction.Down:
            pos_x -= 1
        if self.direction == Direction.Left:
            pos_y += 1
        if self.direction == Direction.Up:
            pos_x += 1
            
        return (pos_x, pos_y)
    

    def check_borders(self) -> tuple[int, int]:
        """ Checks if the movable object reached the end of the map
            on any direction
            If the movable reaches the border, returns the moveables new position

        @return:
            (pos_x, pos_y) [int, int] - the player new position
        """
        pos_x = self.position[0]
        pos_y = self.position[1]
        
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