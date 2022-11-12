from abc import ABC, abstractmethod
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import Coordinates


class Canvas(ABC):
    @abstractmethod
    def draw_dots(self, coordinates: List[Coordinates], obj_type: str = None):
        """

        :param coordinates:
        :param obj_type:
        :return:
        """
        pass

    @abstractmethod
    def render(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def clear(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_height(self):
        """

        :return:
        """
        pass

    @abstractmethod
    def get_width(self):
        """

        :return:
        """
        pass
