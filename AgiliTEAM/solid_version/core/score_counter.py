from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pellets import Pellets
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman import Pacman


class ScoreCounter(GameElement):

    def __init__(self,
                 base_score: int,
                 difficulty: float,
                 pacman: Pacman,
                 pellets: Pellets,
                 ):
        self.score_pellet = base_score * difficulty
        self.pacman = pacman
        self.pellets = pellets

        self.score = 0

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        for i in range(len(self.pellets.pos)):
            if self.pacman.pos[0] == self.pellets.pos[i]:
                self.score += self.score_pellet
                self.pellets.pos.pop(i)
                break

        return True
