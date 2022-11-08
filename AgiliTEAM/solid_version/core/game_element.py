from abc import ABC, abstractmethod

from solid_version.core.key_event import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent):
        pass

    @abstractmethod
    def tick(self) -> bool:
        pass
