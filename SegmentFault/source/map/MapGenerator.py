"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapGenerator.py
/ AUTHOR       : Gergely Őri
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module is responsible for map generation related tasks, handles
  and handles obsticle detecting

/*********************************************************************
/*********************************************************************
"""
from typing import List

from MapElements import MapElements

class MapGenerator:
    def __init__(self, dataset=None):
        if dataset==None:
            self.generate_basic_map()
        else:
            self.dataset=dataset
        self.map_elements=MapElements.list_value()
        self.element_names=MapElements.list_name()
        self.element_coordinates=[[] for element_count in range(len(self.map_elements))]
        self.translate_dataset()

    def translate_dataset(self):
         for map_row in range(len(self.dataset)):
             for map_column in range(len(self.dataset[map_row])):
                 for element_count in range(len(self.map_elements)):
                    if self.dataset[map_row][map_column]==self.map_elements[element_count]:
                     self.element_coordinates[element_count].append([map_row,map_column])

    def get_coordinates(self)-> list[list[tuple[int,int]]]:
        return self.element_coordinates

    def get_obsacle_coordinates(self, obstacle: MapElements) ->list[tuple[int,int]]:
        if obstacle.name in self.element_names:
            return self.element_coordinates[self.element_names.index(obstacle.name)]

    def generate_basic_map(self):
        """ Generate a 27*27 size Map, walls on the borders of the map and points inside the borders

            @args:
            self
        """
        first_and_last_row = MapElements.Wall.value * 27
        inner_row = MapElements.Wall.value+MapElements.Point.value*25+MapElements.Wall.value
        self.dataset = [first_and_last_row, inner_row,first_and_last_row]
        for added_row in range(len(first_and_last_row)-3):
            self.dataset.insert(1,inner_row)

    def get_mapsize(self)-> list[int]:
        return [len(self.dataset[0]), len(self.dataset)]

    def contains_obstacle(self, obstacle:MapElements)->bool:
        for row_index in range(len(self.dataset)):
            if obstacle.value in self.dataset[row_index]:
                return True

        return False