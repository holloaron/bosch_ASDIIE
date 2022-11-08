from typing import List

from solid_version.core.game_element import GameElement
from solid_version.core.key_event import KeyEvent

from solid_version.core.ghosts import Ghosts
from solid_version.core.pacman import Pacman



class PacmanGameState:

    def __init__(self, game_elements: List[GameElement]):
        self.game_elements = game_elements
        self._can_game_continue = True

    def step(self):
        current_pacman_pos = None
        for game_element in self.game_elements:
            if isinstance(game_element,Pacman):
                self._can_game_continue = self._can_game_continue and game_element.tick()
                current_pacman_pos = game_element.get_pacman_position()
                continue
            elif isinstance(game_element,Ghosts):
                self._can_game_continue = self._can_game_continue and game_element.tick(current_pacman_pos)
                continue
            else:
                self._can_game_continue = self._can_game_continue and game_element.tick()

    def is_terminated(self):
        return not self._can_game_continue

    def take_action(self, key_event: KeyEvent):
        for game_element in self.game_elements:
            if isinstance(game_element, Ghosts):
                continue
            game_element.take_action(key_event)
