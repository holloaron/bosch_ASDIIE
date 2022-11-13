from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pellets import Pellets
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pacman import Pacman


class ScoreCounter(GameElement):

    def __init__(self,
                 base_score: int,
                 difficulty: float,
                 pacman: Pacman,
                 pellets: Pellets,
                 ):
        """

        :param base_score:
        :param difficulty:
        :param pacman:
        :param pellets:
        """
        self.score_pellet = base_score * difficulty
        self.pacman = pacman
        self.pellets = pellets

        self.score = 0

    def take_action(self, key_event: KeyEvent) -> None:
        pass

    def tick(self) -> bool:
        """

        :return:
        """
        for pos in range(len(self.pellets.pos)):
            if self.pacman.pos[0] == self.pellets.pos[pos]:
                self.score += self.score_pellet
                self.pellets.pos.pop(pos)
                break

        return True
