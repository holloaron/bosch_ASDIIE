import os


class Visualizer:
    def __init__(self):
        self.observation = None

    def clear_console(self):
        # Clearing console before printing the map (cannot clear the console in PyCharm, only in terminal)
        os.system('cls' if os.name == 'nt' else 'clear')

    def process_observation(self, observation):
        # Converting numpy array to python list
        self.observation = observation.tolist()

    def render(self):
        # Printing the current score and the current observation line by line with separation
        for line in self.observation:
            print(*line, sep='  ')

    def show_score(self, curr_score: int):
        """
        Informing the user about the current score
        :param curr_score: Current score of the player (int)
        :return: -
        """
        print("\nCurrent score:", curr_score)
