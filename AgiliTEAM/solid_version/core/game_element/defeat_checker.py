from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pacman import Pacman


class DefeatChecker(GameElement):

    def __init__(self,
                 pacman: Pacman,
                 ghosts: Ghosts,
                 ):
        """

        :param pacman:
        :param ghosts:
        """
        self.pacman = pacman
        self.ghosts = ghosts

    def take_action(self, key_event: KeyEvent) -> None:
        """

        :param key_event:
        :return: None
        """
        pass

    def tick(self) -> bool:
        """

        :return:
        """
        for i in range(len(self.ghosts.pos)):
            if self.pacman.pos[0] == self.ghosts.pos[i]:
                return False

        return True
