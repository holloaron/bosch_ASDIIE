from typing import List

from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.game_element import GameElement
from bosch_ASDIIE_Git_egylet.Git_egylet.solid_version.core.key_event import KeyEvent


class PacmanGameState:
    def __init__(self, game_elements: List[GameElement]):
        self.game_elements = game_elements
        self._can_game_continue = True

    def step(self):
        for game_element in self.game_elements:
            self._can_game_continue = self._can_game_continue and game_element.tick()