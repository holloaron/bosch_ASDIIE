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
from Direction import *

class Player():
    def __init__(self, start_position = (0,0), start_direction = Direction.Down) -> None:
        self.direction = start_direction
        self.position = start_position
        self.X = self.position[0]
        self.Y = self.position[1]
        self.is_dead = False
        self.score = 0