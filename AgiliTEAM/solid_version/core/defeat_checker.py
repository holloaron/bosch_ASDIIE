from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman import Pacman


class DefeatChecker(GameElement):

    def __init__(self,
                 pacman: Pacman,
                 ghosts: Ghosts,
                 ):
        self.pacman = pacman
        self.ghosts = ghosts

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        for i in range(len(self.ghosts.pos)):
            if self.pacman.pos[0] == self.ghosts.pos[i]:
                return False

        return True
