MAP_SIZE = 30

class Pacman:
    """

    """
    def __init__(self):
        self.map_size = MAP_SIZE

        self.coins = []
        self.ghosts = []

        self.step = 0
        self.score = 0
        self.orientation = 0
        self.state = None
