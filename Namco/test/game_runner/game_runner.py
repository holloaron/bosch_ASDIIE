import unittest
from bosch_ASDIIE.Namco.map import Map
from bosch_ASDIIE.Namco.pac_man import PacMan
from bosch_ASDIIE.Namco.visualizer import Visualizer
from bosch_ASDIIE.Namco.game_runner import GameRunner
from bosch_ASDIIE_Namco.Namco.game_element import GameElement
from bosch_ASDIIE_Namco.Namco.key_event import KeyEvent
from bosch_ASDIIE_Namco.Namco.pacman_game_state import PacmanGameState


class GameElementIsCalledMock(GameElement):
    def __init__(self):
        self.is_take_action_called = False
        self.is_tick_called = False

    def take_action(self, key_event: KeyEvent):
        self.is_take_action_called = True

    def tick(self):
        self.is_tick_called = True


def test_whenTakeAction_thenGameElementsGetIt():
    game_element_mock = GameElementIsCalledMock()
    snake_game_state = PacmanGameState([game_element_mock])
    snake_game_state.take_action(KeyEvent.UP)
    assert game_element_mock.is_take_action_called, \
        "After the take_action called, the child GameElement objects" \
        " should get the key event."


class MyTestCase(unittest.TestCase):
    def testGameRunner_whenStepCounterReachesLimit_GameTerminates(self):
        test_game_runner = GameRunner(agent=PacMan(x=6, y=6),
                                 world=Map("map.txt"),
                                 visualizer=Visualizer(),
                                 max_step_num=100)
        pacman_game_state = PacmanGameState([PacMan()])
        for step_cnt in range(50):
            pacman_game_state.take_action(KeyEvent.LEFT)
            pacman_game_state.step()
            pacman_game_state.take_action(KeyEvent.RIGHT)
            pacman_game_state.step()
        done = test_game_runner._step
        self.assertTrue((test_game_runner.step_num == 100) & (done == True))
        "When Pacman moves 100 times, the game should terminate" \
        "(done flag actives)"


if __name__ == '__main__':
    unittest.main()
