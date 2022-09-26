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
    def __init__(self, start_position: tuple[int, int], start_direction: Direction):
        self.direction = start_direction
        self.position = start_position
        self.is_dead = False
        self.score = 0