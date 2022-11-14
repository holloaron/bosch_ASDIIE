import unittest
from bosch_ASDIIE.Namco.map import Map
from bosch_ASDIIE.Namco.pac_man import PacMan

class TestCase(unittest.TestCase):
    def test_whenTheGameBegins_PacmanIsAtTheRightPosition(self):
        agent = PacMan(6,6)
        test_world = Map("map.txt")
        test_world.update_map([agent.x,agent.y],False)
        self.assertEqual(test_world.map[agent.x, agent.y], '0')
        "When the game begins, Pacman should be at [6,6] on the map"


    def test_whenWallIsHit_PacmanDies(self):
        agent = PacMan(6,6)
        test_world = Map("map.txt")
        agent.process_action('w')
        test_dot_coll, test_wall_coll = test_world.check_collision([agent.x,agent.y])
        self.assertTrue(test_wall_coll,msg="Wall hit")
        "When a wall is hit, Pacman should die"

    def test_whenDotIsHit_DotCounterIncreases(self):
        agent = PacMan(6,6)
        test_world = Map("map.txt")
        agent.process_action('a')
        test_dot_coll, test_wall_coll = test_world.check_collision([agent.x,agent.y])
        self.assertTrue(test_dot_coll,msg="Dot hit")
        "When a dot is hit, the score counter flag should be active"

if __name__ == '__main__':
    unittest.main()
