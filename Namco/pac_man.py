class PacMan:
    def __init__(self):
        """
        Implements PacMan
        """
        self.row = 0
        self.col = 0

    def process_action(self, action: str) -> [int, int]:
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

        return self.row, self.col
