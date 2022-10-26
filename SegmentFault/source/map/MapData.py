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

from source.map import MapElements

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