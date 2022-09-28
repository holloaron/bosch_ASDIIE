import pygame

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900

COLOR_YELLOW = pygame.Color(255, 255, 0)


class Pacman:

    def __init__(self):
        self.pacman_position = [50, 50]

        pygame.init()
        pygame.display.set_caption('TeamSix Pacman')
        self.game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def play(self):
        while True:
            self.draw_on_screen()
            pygame.display.update()

    def draw_on_screen(self):
        pygame.draw.circle(self.game_window, COLOR_YELLOW, (self.pacman_position[0] + 15, self.pacman_position[1] + 15),
                           15)


if __name__ == '__main__':
    game = Pacman()
    game.play()
