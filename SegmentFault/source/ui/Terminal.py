"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Terminal.py
/ AUTHOR       : 
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
import InputParser, Inputs

class Terminal():

    @staticmethod
    def show_menu(menutitle: str, menuitems: dict[str, str]) -> None:
        """ Displays the given menu
        @args:
            menutitle [str] - the title of the current menu
            menuitems [dict(str, str)] - dictionary containing the menuitems
        """
        print(menutitle)
        for i in menuitems:
            print(f"\t{i.key}. {i.value}")


    @staticmethod
    def show_gameplayresult() -> None:
        """ Displayes the gameplay results
        @args:

        """
        pass


    @staticmethod
    def show_title() -> None:
        """ Displayes the gametitle from local file
        """
        current_dir = os.path.dirname(__file__)
        title_source_path = os.path.relpath("..\\data\\assets\\TerminalTitle.txt", current_dir)
        title = open(title_source_path, 'r')

        while True:
            line = title.readline()

            # EndOfFile
            if not line:
                break

            print(line)


    @staticmethod
    def clear() -> None:
        """ Clears the console
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    @staticmethod
    def get_menu_input(massage: str, menuitems: dict[str, str]) -> str:
        """ Returns the parsed input from the user for menu contol

        @args:
            massage [str] - displayed massage for user
            menuitems [dict(str, str)] - dictionary containing the menuitems
        @return:
            parsed_input [str] - response from user
        """
        parsed_input = InputParser.parse(input(f"{massage}\n"), menuitems.keys())

        if parsed_input is Inputs.Nothing:
            parsed_input = InputParser.parse(input(f"{massage}\n"), menuitems.values())

        return parsed_input

    @staticmethod
    def get_gameplay_input(massage: str) -> str:
        """ Returns the parsed input from the user for gameplay control

        @args:
            massage [str] - displayed massage for user
        @return:
            parsed_input [str] - response from user
        """
        parsed_input = InputParser.parse(input(f"{massage}\n"))

        return parsed_input

    