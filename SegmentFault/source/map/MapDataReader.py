"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapDataReader.py
/ AUTHOR       : Gergely Őri
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Data provider, from selected local .mapdat files, or with a basic
map

/*********************************************************************
/*********************************************************************
"""

import os
from typing import Callable, List

from MapElements import MapElements
from MapData import MapData
from MapGenerator import MapGenerator

class MapDataReader:

    def __init__(self) -> None:
        self.data_set = None

    @staticmethod
    def list_mapdatas(self) -> list[str]:
        """ Gathers the available .mapdat filenames

        @returns:
            mapdata_files [list(str)]
        """
        mapdata_files = []

        current_dir = os.path.dirname(__file__)
        mapdata_dir = os.path.join(current_dir, "data/maps")
        for mapdat in os.listdir(mapdata_dir):
            mapdata_files.append(mapdat)
        
        return mapdata_files


    def fill_mapdata(self, map=None):
        """ Fills a MapData member with data

        @args:
            map [str] - label of the choosen map
        @returns:
            mapdata [MapData] - class member holding the mapdata
        """
        mapdata = None
        mapdatafile_path = None
        if not map is None:
            mapdata_paths = self.list_mapdatas()
            for item in mapdata_paths:
                # if the path contains the map string
                if item.find(map) != -1:
                    mapdatafile_path = item
            self.data_set = self.load_mapdata(mapdatafile_path)

        #TODO: fill mapdata
        

    def load_mapdata(self, mapdatafile_path: str) -> list[list[str]]:
        """ Loads the mapdata from the file of the given path as lol(str)

        @args:
            self
            mapdatafile_path [str] - path for the mapdata file
        @return:
            lines [List[List[str]]] - list of list containing the mapdata
        """
        mapdata = open(mapdatafile_path, 'r')

        lines = []

        while True:
            line = mapdata.readline()

            # EndOfFile
            if not line:
                break

            if list(line)[-1] == '\n':
                lines.append(list(line)[:-1])
            else:
                lines.append(list(line))

        mapdata.close()

        return lines


    def get_size(self) -> tuple[(int, int)]:
        """ Determines the loaded mapsize

        @args:
            self
        @return:
            size [tuple(int, int)] - [0] - width of the map
                                     [1] - height of the map
        """
        map_height = len(self.data_set)
        map_width = 0

        for i in range(len(self.data_set)):
            if len(self.data_set[i]) > map_width:
                map_width = len(self.data_set[i])

        return (map_width, map_height)


    def contains(self, element: MapElements) -> bool:
        """ Determines if the map contains the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @return:
            result [bool] - True, if the mapdata contains the given MapElement
        """
        for i in range(len(self.data_set)):
            if element in self.data_set[i]:
                return True

        return False


    def get_first_coord_of(self, element: MapElements) -> tuple[(int, int)]:
        """ Returns the coordinates of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            result [tuple(x [int], y [int])] - the first found coordinate          
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        x = 0
        y = 0
        
        for i in range(len(self.data_set)):

            y = 0
            for j in self.data_set[i]:
                if j == element.value:
                    return (x,y)
                y += 1

            x +=1
        
            

    def get_coords_of(self, element: MapElements) -> list[(int,int)]:
        """ Returns a list of coordinates as tuple of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            result [list[tuple(int,int)]] - the found coordinates on the map
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        result = []
        x = 0
        y = 0
        
        for i in range(len(self.data_set)):

            y = 0
            for j in self.data_set[i]:
                if j == element.value:
                    result.append((x,y))
                y += 1

            x +=1

        return result