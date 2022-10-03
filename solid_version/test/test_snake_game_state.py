from bosch_ASDIIE.solid_version.core.game_element import GameElement
from bosch_ASDIIE.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.solid_version.core.snake_game_state import SnakeGameState
from bosch_ASDIIE.solid_version.core.snake import Snake


def test_WhenOneStep_IsTerminatedFalse():
    snake_game_state = SnakeGameState([])
    snake_game_state.step()
    assert not snake_game_state.is_terminated(), \
        "The initialized game should not step into terminated state."


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
    snake_game_state = SnakeGameState([game_element_mock])
    snake_game_state.take_action(KeyEvent.UP)
    assert game_element_mock.is_take_action_called, \
        "After the take_action called, the child GameElement objects" \
        " should get the key event."


def testSnakeGameState_whenStep_thenGameElementsTickCalled():
    game_element_mock = GameElementIsCalledMock()
    snake_game_state = SnakeGameState([game_element_mock])
    snake_game_state.step()
    assert game_element_mock.is_tick_called, \
        "After the step function called, tick function of " \
        "the child GameElement objects should be called."


def testSnakeGameState_whenSnakeBitesItself_thenGameStateIsTerminated():
    snake_game_state = SnakeGameState([Snake()])
    snake_game_state.take_action(KeyEvent.UP)
    snake_game_state.step()
    snake_game_state.take_action(KeyEvent.LEFT)
    snake_game_state.step()
    snake_game_state.take_action(KeyEvent.DOWN)
    snake_game_state.step()
    assert snake_game_state.is_terminated(), \
        "Snake turn around and bites itself, so the " \
        "game step into a terminated GameState."


def testSnakeGameState_whenSnakeMovesOneDirectionAfterInit_thenGameStateIsNotTerminated():
    snake_game_state = SnakeGameState([Snake()])
    for _ in range(5):
        snake_game_state.step()
    assert not snake_game_state.is_terminated(), \
        "When snake moves in one direction and it is short, " \
        "then it does not die."
    for _ in range(50000):
        snake_game_state.step()
    assert not snake_game_state.is_terminated(), \
        "When snake moves in one direction and it is short, " \
        "then it does not die."
