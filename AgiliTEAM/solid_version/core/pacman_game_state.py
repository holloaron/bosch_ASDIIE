from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pacman import Pacman
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.walls import Walls


class PacmanGameState:

    def __init__(self, game_elements: List[GameElement]):
        """

        :param game_elements:
        """
        self.game_elements = game_elements
        self._can_game_continue = True

    def step(self) -> None:
        """

        :return: None
        """
        current_pacman_pos = None
        for game_element in self.game_elements:
            if isinstance(game_element, Pacman):
                self._can_game_continue = self._can_game_continue and game_element.tick()
                current_pacman_pos = game_element.get_pacman_position()
                continue
            elif isinstance(game_element, Ghosts):
                self._can_game_continue = self._can_game_continue and game_element.tick(current_pacman_pos)
                continue
            elif isinstance(game_element, Walls):
                self._can_game_continue = self._can_game_continue and game_element.tick(current_pacman_pos)
                continue
            else:
                self._can_game_continue = self._can_game_continue and game_element.tick()

    def is_terminated(self) -> bool:
        """

        :return:
        """
        return not self._can_game_continue

    def take_action(self, key_event: KeyEvent) -> None:
        """

        :param key_event:
        :return: None
        """
        for game_element in self.game_elements:
            if isinstance(game_element, Ghosts):
                continue
            game_element.take_action(key_event)
