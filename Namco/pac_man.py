class PacMan:
    def __init__(self):
        self.row = 0
        self.col = 0

    def process_action(self, action: str) -> None:
        """
        Moves PacMan in the desired direction
        :param action: current user input (w, a, s or d) (str)
        :return: -
        """
        # Moving up
        if action == 'w':
            self.row -= 1
        # Moving left
        elif action == 'a':
            self.col -= 1
        # Moving down
        elif action == 's':
            self.row += 1
        # Moving right
        elif action == 'd':
            self.col += 1
