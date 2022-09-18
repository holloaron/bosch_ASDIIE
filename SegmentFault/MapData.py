"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : TimerThread.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Timer module to measure and handle time while the program is running

/*********************************************************************
/*********************************************************************
"""

from enum import Enum
from operator import contains
class MapElements(str, Enum):
    Wall = '#'
    Place = '_'
    Door = '-'
    Point = ' '
    Coin = 'o'
    PacMan = 'O'
    Blinky = 'R' # red ghost
    Pinky = 'P'  # pink ghost
    Inky = 'I'   # cyan ghost
    Clyde = 'C'  # orange ghost

"""
/*********************************************************************
"""

class MapData():
    def __init__(self, MapDataFilePath):
        self.data_path = MapDataFilePath
        self.size = self.get_size()
        self.height = self.size[0]
        self.width = self.size[1]
        
    """
    get_size method
    Returns the mapsize as a tuple
        [0] - height
        [1] - width
    """
    def get_size(self):
        mapdata = open(self.data_path, 'r')

        height = 0
        width = 0

        while True:
            line = mapdata.readline()

            if not line:
                break

            height += 1
            current_width = len(line)
            if current_width > width:
                width = current_width

        mapdata.close()
        return (height, width)

    """
    contains method
    Returns true, if the mapdata contains the given MapElement
    """
    def contains(self, element):
        mapdata = open(self.data_path, 'r')

        result = False

        while True:
            line = mapdata.readline()

            if not line:
                break

            for i in line:
                if i == element.value:
                    result = True
                    break

        mapdata.close()
        return result


    """
    get_coordinate
    Returns the first coordinate as tuple of the given element
        [1] - pos_X
        [2] - pos_Y
    """
    def get_first_coord_of(self, element):

        if not self.contains(element):
            raise Exception(f"The Map does not contain the given element: {element.name} {element.value}")

        mapdata = open(self.data_path, 'r')
        x = 0
        y = 0

        while True:
            line = mapdata.readline()

            if not line:
                break

            y = 0
            for i in line:
                if i == element.value:
                    mapdata.close()
                    return (x,y)
                y += 1
            
            x +=1
            
    """
    get_coords
    Returns a list of coordinates as tuple of the given MapElement

    If the list id empty,
    the Map does not contains the given MapElement
    """
    def get_coords_of(self, element):
        mapdata = open(self.data_path, 'r')
        
        result = []
        x = 0
        y = 0
        
        while True:
            line = mapdata.readline()

            if not line:
                break

            y = 0
            for i in line:
                if i == element.value:
                    result.append((x,y))
                y += 1
            
            x += 1

        mapdata.close()
        return result