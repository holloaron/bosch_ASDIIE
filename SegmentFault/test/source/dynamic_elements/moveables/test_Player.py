"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : test_Moveable.py
AUTHOR       : 
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
source/dynamic_elements/moveables/Moveable.py testing module

To run this module:
python3 -m unittest test.source.dynamic_elements.moveables.test_Player

see README for help
********************************************************************
********************************************************************
"""

import unittest

from source.dynamic_elements.moveables.Player import Player
from source.map.MapData import MapData
from source.dynamic_elements.Direction import Direction

class test_Moveable(unittest.TestCase):

    def test_set_score(self):
        """
        """
        mapdata = MapData()
        mapdata.collectables.points = [(1,1)]
        mapdata.collectables.coins = [(2,2)]

        player = Player(mapdata, (0,0), Direction.Down)
        
        # no collectable on the players position
        self.assertEqual(player.set_score(), 0)
        # point
        player.position = (1,1)
        self.assertEqual(player.set_score(), 10)
        # coin
        player.position = (2,2)
        self.assertEqual(player.set_score(), 20)

        #TODO: cherry and ghost implementation



if __name__ == "__main__":
    unittest.main()