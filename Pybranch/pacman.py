import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()


class Dot(pygame.sprite.Sprite):
    def __init__(self):
        self.frame_min = 40
        self.frame_max = 960
        self.dot_size = (20, 20)
        self.dot_number = 60

        # Loading the Dot from file and transform to the required size

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, self.dot_size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.frame_min, self.frame_max)
        self.rect.y = random.randint(self.frame_min, self.frame_max)

    def dot_creation(self, dot_sprite: pygame.sprite.Group, every_sprite: pygame.sprite.Group):
        """
            Create an appropriate number of dots

        @args:
            dot_sprite [Group]-the group of dots
            every_sprite [Group]-the group of all elements
        """
        self.dot_sprite = dot_sprite
        self.every_sprite = every_sprite
        for i in range(self.dot_number):
            dot_score = Dot()
            self.dot_sprite.add(dot_score)
            self.every_sprite.add(dot_score)


class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        self.pos_x = 160
        self.pos_y = 520
        self.speed = 5
        self.size = (50, 50)

        # Loading the PacMan from file and transform to the required size

        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def move(self, screen_height: int, screen_width: int):
        """
            Moves the PacMan using the arrow keys and when it
            reaches the edge of the screen it moves to the other side

        @args:
            (screen_height, screen_width) [int, int]-the screen size
        """

        self.screen_height = screen_height
        self.screen_width = screen_width

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
            if self.rect.top < 0:
                self.rect.move_ip(0, self.screen_height)
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            if self.rect.bottom > self.screen_height:
                self.rect.move_ip(0, -self.screen_height)
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            if self.rect.left < 0:
                self.rect.move_ip(self.screen_width, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            if self.rect.right > self.screen_width:
                self.rect.move_ip(- self.screen_width, 0)


class Screen():
    def __init__(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)

        self.screen_size = 1000
        self.time_pos = 950
        self.score_pos = 10
        self.score = 0
        self.max_time = 45000
        self.game_over_pos_x = 320
        self.game_over_pos_y = 500

        self.font_size = 60
        self.font_size_small = 20
        self.font = pygame.font.SysFont("Verdana", self.font_size)
        self.font_small = pygame.font.SysFont("Verdana", self.font_size_small)
        self.game_over = self.font.render("Game Over", True, self.yellow)

        self.DISPLAYSURF = pygame.display.set_mode((self.screen_size, self.screen_size))

    def starting_window_creation(self):
        """
            Show the start of the game scene
        """
        self.DISPLAYSURF.fill(self.black)
        pygame.display.set_caption("PACMAN")

    def game_window(self):
        """
            Show the game scene
        """
        self.DISPLAYSURF.fill(self.black)
        current_score = self.font_small.render(str(self.score), True, self.white)
        current_time = self.font_small.render(str(game_time), True, self.white)
        self.DISPLAYSURF.blit(current_score, (self.score_pos, self.score_pos))
        self.DISPLAYSURF.blit(current_time, (self.time_pos, self.score_pos))

    def game_over_window(self):
        """
            Show the end of game scene
        """
        self.DISPLAYSURF.fill(self.black)
        self.DISPLAYSURF.blit(self.game_over, (self.game_over_pos_x, self.game_over_pos_y))

    def sprite_draw(self, any_sprite):
        """
            Display a group on the screen
        @args:
            any_sprite [Group]- group to be displayed
        """
        self.any_sprite = any_sprite
        self.any_sprite.draw(self.DISPLAYSURF)

    def pacman_dot_collison(self, player: PacMan, dot: Dot, dots_sprite: pygame.sprite.Group) -> None:
        """
            If the PackMan picks up the points it increase the score
        @args:
            player [PacMan] - The PacMan class
            dot [Dot] - The Dot class
            dots_sprite - The group of dots
        """
        self.player = player
        self.dot = dot
        self.dots_sprite = dots_sprite
        dot_hit_list = pygame.sprite.spritecollide(self.player, dots_sprite, True)

        for self.dot in dot_hit_list:
            self.score += 1


if __name__ == "__main__":
    Pac_man = PacMan()
    Dots = pygame.sprite.Group()
    All_Sprites = pygame.sprite.Group()
    Window = Screen()
    Window.starting_window_creation()
    Score_Dot = Dot()
    Score_Dot.dot_creation(Dots, All_Sprites)
    All_Sprites.add(Pac_man)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game_time = round(((Window.max_time - pygame.time.get_ticks()) / 1000),
                          2)  # Time available until the end of game
        Window.game_window()
        Pac_man.move(Window.screen_size, Window.screen_size)
        Window.pacman_dot_collison(Pac_man, Score_Dot, Dots)
        Window.sprite_draw(All_Sprites)
        if Window.score == Score_Dot.dot_number or game_time <= 0:  # If the game is over
            time.sleep(0.5)
            Window.game_over_window()
            pygame.display.update()
            for entity in All_Sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        FramePerSec.tick(FPS)

