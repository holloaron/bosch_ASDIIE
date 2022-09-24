"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapData.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Position data provider, from a local .dat file

/*********************************************************************
/*********************************************************************
"""

from enum import Enum

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
/*********************************************************************
"""

class MapData():
    def __init__(self, MapDataFilePath: str):
        self.data_path = MapDataFilePath
        self.size = self.get_size()
        self.height = self.size[0]
        self.width = self.size[1]
        

    def get_size(self) -> tuple(int,int):
        """ Determines the loaded mapsize

        @args:
            self
        @return:
            map_height [int] - height of the map
            map_width [int] - width of the map
            size [tuple(int,int)] - [0] - height
                                    [1] - width
        """
        mapdata = open(self.data_path, 'r')

        map_height = 0
        map_width = 0

        while True:
            line = mapdata.readline()

            # eof
            if not line:
                break

            map_height += 1
            current_width = len(line)
            if current_width > map_width:
                map_width = current_width

        mapdata.close()
        return (map_height, map_width)

    def contains(self, element: MapElements) -> bool:
        """ Determines if the map contains the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @return:
            result [bool] - True, if the mapdata contains the given MapElement
        """
        mapdata = open(self.data_path, 'r')

        result = False

        while True:
            line = mapdata.readline()

            # eof
            if not line:
                break

            for i in line:
                if i == element.value:
                    result = True
                    break

        mapdata.close()
        return result


    def get_first_coord_of(self, element: MapElements) -> tuple(int,int):
        """ Returns the coordinates of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            tuple(x [int], y [int]) - the first             
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        mapdata = open(self.data_path, 'r')

        x = 0
        y = 0

        while True:
            line = mapdata.readline()

            # eof
            if not line:
                break

            y = 0
            for i in line:
                if i == element.value:
                    mapdata.close()
                    return (x,y)
                y += 1
            
            x +=1
            
    def get_coords_of(self, element: MapElements) -> list[tuple(int,int)]:
        """ Returns a list of coordinates as tuple of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            result [list[tuple(int,int)]] - 
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        mapdata = open(self.data_path, 'r')
        
        result = []
        x = 0
        y = 0
        
        while True:
            line = mapdata.readline()

            #eof
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