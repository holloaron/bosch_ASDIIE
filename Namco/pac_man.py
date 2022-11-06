class PacMan:
    def __init__(self, init_row: int = 6, init_col: int = 6):
        """
        Implements PacMan
        """
        self.row = init_row
        self.col = init_col

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
