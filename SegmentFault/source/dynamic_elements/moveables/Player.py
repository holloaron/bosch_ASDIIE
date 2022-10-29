"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Player.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module responsible for movement and gameplay data

/*********************************************************************
/*********************************************************************
"""

from source.dynamic_elements.moveables import Moveable
from source.dynamic_elements import Direction
from source.map import MapData

class Player(Moveable):
    def __init__(self, mapdata: MapData, start_position: tuple[int, int], start_direction: Direction):
        super().___init__(mapdata, start_position, start_direction)
        self.direction = start_direction
        self.position = start_position
        self.is_dead = False
        self.score = 0

    def get_next_position(self) -> tuple[int, int]:
        """ Sets the players new position based on the mapdata, current position and direction
        
        @return:
            (pos_x, pos_y) [int, int] - the player new position
        """
        pos_x = self.position[0]
        pos_y = self.position[1]

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