from abc import ABC, abstractmethod
from typing import List

from core.misc.map import Coordinates


class Canvas(ABC):
    @abstractmethod
    def draw_dots(self, coordinates: List[Coordinates], obj_type: str = None) -> None:
        """

        :param coordinates:
        :param obj_type:
        :return: None
        """
        pass

    @abstractmethod
    def render(self) -> None:
        """

        :return: None
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """

        :return: None
        """
        pass

    @abstractmethod
    def get_height(self) -> int:
        """

        :return:
        """
        pass

    @abstractmethod
    def get_width(self) -> int:
        """

        :return:
        """
        pass
