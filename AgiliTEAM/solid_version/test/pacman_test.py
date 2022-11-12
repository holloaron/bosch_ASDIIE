from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman_game_state import PacmanGameState
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pacman import Pacman
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.defeat_checker import DefeatChecker
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pellets import Pellets
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import Coordinates


def test_WhenOneStep_IsTerminatedFalse() -> None:
    """

    :return: None
    """
    pacman_game_state = PacmanGameState([])
    pacman_game_state.step()
    assert not pacman_game_state.is_terminated(), \
        "The initialized game should not step into terminated state."


def test_PacmanStepFunction() -> None:
    """

    :return: None
    """
    pacman = Pacman(body=[Coordinates(5, 5)], map_size=MapSize(10, 10))
    test_game_state = PacmanGameState([pacman])
    test_game_state.take_action(KeyEvent.UP)
    test_game_state.step()
    assert not (pacman.get_pacman_position() == [Coordinates(5, 6)]), \
        "Error during step, value mismatch"


def test_DefeatCheckingBy_IsTerminatedTrue() -> None:
    """

    :return: None
    """
    map_size = MapSize(10, 10)
    num_pellets = 0
    num_ghosts = 99
    pacman = Pacman(map_size=map_size)
    pellets = Pellets(map_size=map_size, num_pellets=num_pellets, known_pos=[pacman.pos])
    ghosts = Ghosts(map_size=map_size, num_ghosts=num_ghosts, known_pos=[pacman.pos, pellets.pos], step_confidence=1.0)
    defeat_checker = DefeatChecker(pacman=pacman, ghosts=ghosts)
    test_game_state = PacmanGameState([pacman, pellets, ghosts, defeat_checker])
    test_game_state.step()
    assert test_game_state.is_terminated(), \
        "The game should have ended due too the number of ghost which makes impossible to escape them."


def test_PacmanCanNotLeaveThePitch_TopLeftCornerPos() -> None:
    """

    :return: None
    """
    pacman = Pacman(body=[Coordinates(1, 1)], map_size=MapSize(3, 3))
    test_game_state = PacmanGameState([pacman])
    test_game_state.take_action(KeyEvent.UP)
    test_game_state.step()
    test_game_state.step()
    test_game_state.step()
    test_game_state.take_action(KeyEvent.LEFT)
    test_game_state.step()
    test_game_state.step()
    test_game_state.step()
    assert not (pacman.get_pacman_position() == [Coordinates(0, 0)]), \
        "Error during step, value mismatch"


def test_NumberOfThePellets() -> None:
    """

    :return: None
    """
    pellets = Pellets(map_size=MapSize(2, 2), num_pellets=3, known_pos=[[Coordinates(0, 0)]])
    assert not (len(pellets.known_pos) - 1 == 3), \
        "Error during step, value mismatch"


def test_PelletGeneration() -> None:
    """

    :return: None
    """
    pellets = Pellets(map_size=MapSize(2, 2), num_pellets=3, known_pos=[[Coordinates(0, 0)]])
    assert not (pellets.pos.count([Coordinates(0, 0)]) == 0), \
        "Error during step, value mismatch"
