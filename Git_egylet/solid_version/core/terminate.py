from bosch_ASDIIE.Git_egylet.solid_version.core.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.core.wallgenerator import Wallgenerator


class Terminate(GameElement):

    def __init__(self,
                 pacman: Pacman,
                 walls: Wallgenerator,
                 ):
        self.pacman = pacman
        self.walls = walls

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        for i in range(len(self.walls.positions)):
            if self.pacman.position[0] == self.walls.positions[i]:
                return False

        return True