class PacMan:
    def __init__(self, x: int = 6, y: int = 6):
        """
        Implements PacMan
        :param x: row that PacMan starts the game at
        :param y: col that PacMan starts the game at
        """
        self.x = x
        self.y = y

    def process_action(self, action: str) -> [int, int]:
        """
        Moves PacMan in the desired direction
        :param action: current user input (w, a, s or d) (str)
        :return: Current x and y coordinate of PacMan [int, int]
        """
        # Moving up
        if action == 'w':
            self.x -= 1
        # Moving left
        elif action == 'a':
            self.y -= 1
        # Moving down
        elif action == 's':
            self.x += 1
        # Moving right
        elif action == 'd':
            self.y += 1

        return self.x, self.y
