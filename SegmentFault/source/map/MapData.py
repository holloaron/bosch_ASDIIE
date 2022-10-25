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

class MapData():
    def __init__(self, mapdatafile_path: str) -> None:
        self.data_set = self.load_mapdata(mapdatafile_path)
        self.size = self.get_size()
        self.width = self.size[0]
        self.height = self.size[1]

        self.obstacles = Obstacles()
        self.obstacles.walls = self.get_coords_of(MapElements.Wall)
        self.obstacles.door = self.get_first_coord_of(MapElements.Door)

        self.collectables = Collectables()
        self.collectables.points = self.get_coords_of(MapElements.Point)
        self.collectables.coins = self.get_coords_of(MapElements.Coin)

        self.enemies = Enemies()
        self.enemies.Blinky = self.get_first_coord_of(MapElements.Blinky)
        self.enemies.Pinky = self.get_first_coord_of(MapElements.Pinky)
        self.enemies.Inky = self.get_first_coord_of(MapElements.Inky)
        self.enemies.Clyde = self.get_first_coord_of(MapElements.Clyde)


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

            if list(line)[-1]== '\n':
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

class Obstacles():
    walls = []
    door = (0,0)

class Collectables():
    points = []
    coins = []

class Enemies():
    Blinky = (0,0) # red ghost
    Pinky = (0,0)  # pink ghost
    Inky = (0,0)   # cyan ghost
    Clyde = (0,0)  # orange ghost