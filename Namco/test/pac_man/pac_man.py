import unittest
from bosch_ASDIIE.Namco.pac_man import PacMan

class MyTestCase(unittest.TestCase):
    def test_whenTheInputIsString_PacmansPositionChanges(self):
        x = 6
        y = 6
        test_pacman = PacMan(x,y)
        test_pacman.process_action('w')
        test_pacman.x, test_pacman.y = test_pacman.position
        self.assertListEqual([x-1,y],[test_pacman.x, test_pacman.y])
        "When the user input is one of the required inputs," \
        "then Pacman's position changes correctly"

    def test_whenTheInputIsNotString_NothingChanges(self):
        x = 6
        y = 6
        test_pacman = PacMan(x,y)
        test_pacman.process_action(True)
        test_pacman.x, test_pacman.y = test_pacman.position
        self.assertListEqual([x,y],[test_pacman.y, test_pacman.y])

        test_pacman = PacMan(x, y)
        test_pacman.process_action(1)
        test_pacman.x, test_pacman.y = test_pacman.position
        self.assertListEqual([x, y], [test_pacman.y, test_pacman.y])
        "When the user input is not one of the required inputs," \
        "then Pacman's position doesn't change"



if __name__ == '__main__':
    unittest.main()
