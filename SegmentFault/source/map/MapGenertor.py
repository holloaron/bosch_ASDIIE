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

class MapGenerator:
    def __init__(self, dataset: list[list[str]]):
        if dataset==None:
            self.generate_basic_map()
        else:
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

    def get_coordinates(self):
        return self.element_coordinates

    def generate_basic_map(self):
        first_and_last_row = MapElements.Wall.value * 27
        inner_row = MapElements.Wall.value
        inner_row=inner_row.join(MapElements.Point.value*25)
        inner_row=inner_row.join(MapElements.Wall.value)
        self.dataset = [first_and_last_row, inner_row,first_and_last_row]
        for added_row in range(len(first_and_last_row)-3):
            self.dataset.insert(1,inner_row)





if __name__ == "__main__":
    db = None
    trial = MapGenerator(db)
    print(trial.element_coordinates)