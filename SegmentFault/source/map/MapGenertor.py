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
/ 

/*********************************************************************
/*********************************************************************
"""

from MapElements import MapElements
import numpy as np

class MapGenerator():
    def __init__(self, dataset: list[list[str]]):
        self.dataset=dataset
        self.mapelements=MapElements.list_value()
        self.element_names=MapElements.list_name()
        self.element_coordinates=[[]for element_count in range(len(self.mapelements))]
        self.translate_dataset()
    def translate_dataset(self):
         for map_row in range(len(self.dataset)):
             for map_column in range(len(self.dataset[map_row])):
                 for element_count in range(len(self.mapelements)):
                    if self.dataset[map_row][map_column]==self.mapelements[element_count]:
                     #print(self.element_names[k])
                     self.element_coordinates[element_count].append([map_row,map_column])



if __name__ == "__main__":
    db = ["o-#", "o-#", "o-#"]
    trial = MapGenerator(db)
    print(trial.element_coordinates)