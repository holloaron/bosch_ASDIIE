"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Terminal.py
/ AUTHOR       : Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module responsible for terminal input and output

/*********************************************************************
/*********************************************************************
"""

import os
from source.ui import InputParser
from source.map import MapDataReader

class Terminal():
    def __init__(self) -> None:
        self.main_menuitems = [
            "start game",
            "game mode",
            "change map",
            "exit"
        ]

        self.gamemode_menuitems = [
            "standard", 
            "sandbox", 
            "back"
        ]

        self.changemap_menuitems = MapDataReader.list_mapdatas()
        self.changemap_menuitems.add("back")

        self.title = self.get_title()


    def show_menu(self, menutitle: str, menuitems: list[str]) -> None:
        """ Displays the given menu
        @args:
            menutitle [str] - the title of the current menu
            menuitems [list(str)] - list containing the menuitems
        """
        self.clear()
        self.show_title()

        print(menutitle)
        index = 0
        for item in menuitems:
            item = os.path.split(index)[1]
            print(f"\t{index}. {item[:-7]}")
            index += 1


    def show_gameplayresult(self) -> None:
        """ Displayes the gameplay results
        @args:

        """
        self.clear()
        self.show_title()

        pass


    def get_title(self):
        """ Loads the title from local file
        """
        current_dir = os.path.dirname(__file__)
        title_source_path = os.path.relpath("..\\data\\assets\\TerminalTitle.txt", current_dir)
        title_source = open(title_source_path, 'r')
        title = []

        while True:
            line = title_source.readline()

            # EndOfFile
            if not line:
                break

            if list(line)[-1]== '\n':
                title.append(list(line)[:-1])
            else:
                title.append(list(line))

        title_source.close()
        
        return title


    def show_title(self) -> None:
        """ Displayes the gametitle
        """
        for line in self.title:
            print(line)      


    def clear(self) -> None:
        """ Clears the console
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)


    def get_menu_input(massage: str, menuitems: list[str]) -> str:
        """ Returns the parsed input from the user for menu contol

        @args:
            massage [str] - displayed massage for user
            menuitems [list(str)] - list containing the menuitems
        @return:
            parsed_input [str] - response from user
        """
        parsed_input = InputParser.parse(input(f"{massage}\n"), menuitems)

        return parsed_input


    def get_gameplay_input(massage: str) -> str:
        """ Returns the parsed input from the user for gameplay control

        @args:
            massage [str] - displayed massage for user
        @return:
            parsed_input [str] - response from user
        """
        parsed_input = InputParser.parse(input(f"{massage}\n"))

        return parsed_input