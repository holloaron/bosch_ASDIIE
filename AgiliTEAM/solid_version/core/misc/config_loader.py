import os
from argparse import Namespace
import yaml
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import Coordinates


class ConfigLoader:

    def __init__(self, file_name):
        """

        :param file_name:
        """
        self.file_name = file_name

    def load_config(self) -> Namespace:
        """

        :return:
        """
        path = os.path.abspath(self.file_name)
        with open(path) as file:
            conf_dict = yaml.load(file, Loader=yaml.FullLoader)

        conf_dict['internal_walls'] = self.get_internal_walls_coordinates(conf_dict['internal_walls'])

        return Namespace(**conf_dict)

    @staticmethod
    def get_internal_walls_coordinates(coordinates_list: list) -> List[Coordinates]:
        pos_list = []
        for coordinate_pair in coordinates_list:
            pos_list.append(Coordinates(coordinate_pair[0], coordinate_pair[1]))

        return pos_list
