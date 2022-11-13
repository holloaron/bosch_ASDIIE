from abc import ABC, abstractmethod

from core.key_interaction.key_event import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent) -> None:
        """

        :param key_event:
        :return: None
        """
        pass

    @abstractmethod
    def tick(self) -> bool:
        """

        :return:
        """
        pass
