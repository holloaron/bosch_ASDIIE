from abc import ABC, abstractmethod

from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent):
        """

        :param key_event:
        :return:
        """
        pass

    @abstractmethod
    def tick(self) -> bool:
        """

        :return:
        """
        pass
