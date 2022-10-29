"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : PacMan.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Driver class and main script for our program

********************************************************************
********************************************************************
"""

import os
import threading
from source import Timer, Config
from source.map.MapData import MapData
from source.ui import Terminal, Inputs
from source.commands import CloseProgramCommand

class PacMan:
    def __init__(self):
        self.terminal = Terminal()
        self.timer = Timer()
        self.config = Config()

        self.show_menu()


    def show_menu(self):
        menuinput = Inputs.Nothing

        while menuinput != "exit":

            self.terminal.show_menu("Main Menu", self.terminal.main_menuitems)
            menuinput = self.terminal.get_menu_input("", self.terminal.main_menuitems)

            # START GAME
            if menuinput == "start game":
                self.start_game_session()

            # GAMEMODE SETTINGS
            if menuinput == "game mode":
                while menuinput != "back":
                    self.terminal.show_menu("Change Gamemode", self.terminal.gamemode_menuitems)
                    menuinput = self.terminal.get_menu_input("Choose gamemode option!", self.terminal.gamemode_menuitems)
                    
                    if menuinput == "standard":
                        #TODO: config handling (standard game mode with loaded maps)
                        pass

                    if menuinput == "sandbox":
                        #TODO: config handling (generated maps)
                        pass

            # MAP SETTINGS
            if menuinput == "change map":
                while menuinput != "back":
                    self.terminal.show_menu("Maps", self.terminal.changemap_menuitems)
                    menuinput = self.terminal.get_menu_input("Choose map option!", self.terminal.changemap_menuitems)
                    
                    #TODO: set config


    def start_game_session(self):

        #TODO: init mapdata based on config
        #TODO: init Player, Ghosts based on config

        mapdata = None


        player_input_thread = threading.Thread(target=self.get_user_input)
        player_input_thread.start()

        game_state = threading.Thread(target=self.render_game_state(mapdata, self.config))
        game_state.start()

        player_input_thread.join()
        game_state.join()


    def get_user_input(self):
        player_input = ""

        while not game_over:
            self.termial.clear()
            self.terminal.show_title()

            self.terminal.get_gameplay_input("Set new direction!")

            if player_input == Inputs.Exit:
                break

    def render_game_state(self, mapdata: MapData):
        #TODO: render game state
        while not game_over:
            pass

    def is_timeout(self, timelimit: int) -> bool:
        """ Determines if the timelimit for the game is passed or not

        @args:
            timelimit [int] - the timelimit for the game
        @return:
            True, if the given timelimit in secunds is up
        """
        if self.Stopper.seconds_passed >= timelimit:
            print(f"You have reached the:  {timelimit} s time limit")
            return True
        else:
            False


    def step(self) -> tuple[any, int, bool]:
        """ Player-Map interaction
        """
        self.player.position = self.set_player_position(self.player.position[0], self.player.position[1])
        self.player.score += self.set_score(self.player.position[0], self.player.position[1])

        obs = self.create_observation()
        self.last_obs = obs

        self.step_ += 1
        if self.step_ > 100:
            self.player.is_dead = True

        return obs.flatten(), self.player.score, self.player.is_dead


    def terminate(self):
        """ Forces the program to shut down
        """
        os._exit(0)

# program entry point
if __name__ == "__main__":
    Game = PacMan()
    game_over = False