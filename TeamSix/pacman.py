import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
PACMAN_SIZE = WINDOW_HEIGHT/20
STEP_SIZE = PACMAN_SIZE
MAX_STEPS = 100

COLOR_YELLOW = pygame.Color(255, 255, 0)
COLOR_BLACK = pygame.Color(0, 0, 0)

POSITION_UP = 'UP'
POSITION_DOWN = 'DOWN'
POSITION_RIGHT = 'RIGHT'
POSITION_LEFT = 'LEFT'

PACMAN_SPEED = 4


class Pacman:

    def __init__(self):
        self.pacman_position = [60, 60]
        self.steps = 0

        self.direction = POSITION_RIGHT
        self.new_direction = self.direction
        pygame.init()
        pygame.display.set_caption('TeamSix Pacman')
        self.game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.fps = pygame.time.Clock()

    def play(self):
        while self.steps < MAX_STEPS:
            self.handle_key_events()
            self.change_direction()
            self.step()
            self.steps += 1

            self.game_window.fill(COLOR_BLACK)
            self.draw_on_screen()
            pygame.display.update()
            self.fps.tick(PACMAN_SPEED)

    def draw_on_screen(self):
        pygame.draw.circle(self.game_window, COLOR_YELLOW, (self.pacman_position[0] + (PACMAN_SIZE/2), self.pacman_position[1] + (PACMAN_SIZE/2)),
                           (PACMAN_SIZE/2))

    def step(self):
        if self.direction == POSITION_UP:
            if self.pacman_position[1] >= STEP_SIZE:
                self.pacman_position[1] -= STEP_SIZE
        if self.direction == POSITION_DOWN:
            if self.pacman_position[1] <= (WINDOW_HEIGHT - (STEP_SIZE+1)):
                self.pacman_position[1] += STEP_SIZE
        if self.direction == POSITION_LEFT:
            if self.pacman_position[0] >= STEP_SIZE:
                self.pacman_position[0] -= STEP_SIZE
        if self.direction == POSITION_RIGHT:
            if self.pacman_position[0] <= (WINDOW_WIDTH - (STEP_SIZE+1)):
                self.pacman_position[0] += STEP_SIZE

    def change_direction(self):
        if self.new_direction == POSITION_UP:
            self.direction = POSITION_UP
        if self.new_direction == POSITION_DOWN:
            self.direction = POSITION_DOWN
        if self.new_direction == POSITION_LEFT:
            self.direction = POSITION_LEFT
        if self.new_direction == POSITION_RIGHT:
            self.direction = POSITION_RIGHT

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.new_direction = POSITION_UP
                if event.key == pygame.K_DOWN:
                    self.new_direction = POSITION_DOWN
                if event.key == pygame.K_LEFT:
                    self.new_direction = POSITION_LEFT
                if event.key == pygame.K_RIGHT:
                    self.new_direction = POSITION_RIGHT


if __name__ == '__main__':
    game = Pacman()
    game.play()
