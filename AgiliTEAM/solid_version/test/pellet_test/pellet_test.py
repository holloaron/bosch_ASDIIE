from solid_version.core.map import Coordinates
from solid_version.core.map import MapSize
from solid_version.core.pellets import Pellets
import unittest

class PelletTest(unittest.TestCase):
    def test_NumberOfThePellets(self):
        pellets = Pellets(map_size=MapSize(2, 2), num_pellets=3, known_pos=[[Coordinates(0, 0)]])
        self.assertFalse(len(pellets.known_pos) == 3,
                         "Error during pellet generation, value mismatch")


    def test_PelletGeneration(self):
        pellets = Pellets(map_size=MapSize(2, 2), num_pellets=3, known_pos=[[Coordinates(0, 0)]])
        self.assertTrue(pellets.pos.count([Coordinates(0, 0)]) == 0, "Error during pellet generation, invalid pellet position")