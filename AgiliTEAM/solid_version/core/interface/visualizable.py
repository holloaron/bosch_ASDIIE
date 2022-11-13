from abc import ABC, abstractmethod

from core.interface.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas) -> None:
        """

        :param canvas:
        :return: None
        """
        pass
