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

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        pass
