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
Ghosts object definitions, movement and modes

********************************************************************
********************************************************************
"""

import Moveable, Direction, GhostMode

class Ghost(Moveable.Movable):
    def __init__(self, start_position: tuple[int, int], start_diretcion: Direction) -> None:
        super(Ghost, self).__init_()
        self.position = start_position
        self.direction = start_diretcion
        self.mode = GhostMode.Roam
        self.root = None


    def Move(self):
        """ Calculates the Ghost next position based on the GhostMode
        
        """
        if self.mode == GhostMode.Roam:
            pass

        if self.mode == GhostMode.Hunt:
            pass

        if self.mode == GhostMode.Fear:
            pass

    
    def generate_new_direction(self):
        """
        
        """

        pass

    
    def is_PacMan_ahead(self) -> bool:
        """ Determines if PacMan is visible for the Ghost

        @return:
            True, if PacMan is in the way of the Ghost
        """
        test_x, test_y = self.get_next_position()

        while not self.is_wall_ahead(test_x, test_y):
            
            return True

        return False


    