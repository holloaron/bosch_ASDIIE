import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()


class Dot(pygame.sprite.Sprite):
    def __init__(self) -> None:
        """
            Create a Dot sprite of the given size with random position
        """
        self.frame_min = 40
        self.frame_max = 960
        self.dot_size = (20, 20)
        # Loading the Dot from file and transform to the required size with random position

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, self.dot_size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.frame_min, self.frame_max)
        self.rect.y = random.randint(self.frame_min, self.frame_max)


class DotCreator:
    def __init__(self) -> None:
        self.collide = Collide()
        self.bool = ListToBool()

    def dot_creator(self, sprite_number: int, sprite_group: pygame.sprite.Group,
                    every_group: pygame.sprite.Group) -> None:
        """
            Create an appropriate number of dots so that they do not conflict with the walls and other dots

        @args:
            sprite_number [int] - the number of dots to create
            sprite_group [Group] - the group of the dots
            every_group [Group] - the group of all sprites
        """

        self.sprite_number = sprite_number
        self.sprite_group = sprite_group
        self.every_group = every_group

        i = 0
        while (i != self.sprite_number):
            self.sprite = Dot()
            self.sprite_wall_collide_list = self.collide.sprite_group_collision(self.sprite, Game_Run.game_scene.walls,
                                                                                False)
            self.sprite_wall_collide = self.bool.list_checker(self.sprite_wall_collide_list)
            self.sprite_dot_collide_list = self.collide.sprite_group_collision(self.sprite, Game_Run.game_scene.dots,
                                                                               False)
            self.sprite_dot_collide = self.bool.list_checker(self.sprite_dot_collide_list)
            if (self.sprite_wall_collide == False and self.sprite_dot_collide == False):
                i += 1
                self.sprite_group.add(self.sprite)
                self.every_group.add(self.sprite)


class DotCreation:
    def __init__(self) -> None:
        self.creation = DotCreator()
        self.dot_number = 60

    def dot_creation(self) -> None:
        """
            Create the points here by calling the dot_creator function
        """
        self.creation.dot_creator(self.dot_number, Game_Run.game_scene.dots, Game_Run.game_scene.every_sprites)


class PacMan(pygame.sprite.Sprite):
    def __init__(self) -> None:
        """
            Create a PacMan sprite of the given size and location
        """
        self.pos_x = 160
        self.pos_y = 520
        self.size = (50, 50)
        self.collide = Collide()
        self.bool = ListToBool()

        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)


class Move:
    def __init__(self) -> None:
        self.speed = 5
        self.border_checking = ScreenBorderChecking()

    def move(self, sprite: pygame.sprite.Sprite, screen_height: int, screen_width: int) -> None:
        """
            Moves the given sprite using the arrow keys

        @args:
            (screen_height, screen_width) [int, int] - the screen sizes
        """
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.sprite = sprite

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.sprite.rect.move_ip(0, -self.speed)

        elif pressed_keys[K_DOWN]:
            self.sprite.rect.move_ip(0, self.speed)

        elif pressed_keys[K_LEFT]:
            self.sprite.rect.move_ip(-self.speed, 0)

        elif pressed_keys[K_RIGHT]:
            self.sprite.rect.move_ip(self.speed, 0)
        self.border_checking.border_checking(self.sprite, self.screen_height, self.screen_width)


class ScreenBorderChecking:

    def border_checking(self, sprite: pygame.sprite.Sprite, screen_height: int, screen_width: int) -> None:
        """
            The other side of the screen displays the movable sprite
        @args:
            sprite [pygame.sprite.Sprite] - the movable sprite
            (screen_height, screen_width) [int, int]-the screen sizes
        """
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.sprite = sprite

        if self.sprite.rect.top < 0:
            self.sprite.rect.move_ip(0, self.screen_height)
        if self.sprite.rect.bottom > self.screen_height:
            self.sprite.rect.move_ip(0, -self.screen_height)
        if self.sprite.rect.left < 0:
            self.sprite.rect.move_ip(self.screen_width, 0)
        if self.sprite.rect.right > self.screen_width:
            self.sprite.rect.move_ip(- self.screen_width, 0)


class Wall(pygame.sprite.Sprite):

    def __init__(self, left: int, top: int, width: int, height: int) -> None:
        """
            Create a wall sprite of the given size and location
        @args:
            (left, top) [int, int] - position of the left side and the top of the wall to be created
            (width, height) [int,int] - the width and height of the wall to be created
        """
        self.width = width
        self.height = height
        self.color = Colors()
        super().__init__()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color.blue)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top


class Screen:
    def __init__(self) -> None:
        self.screen_size = 1000
        self.time_pos = 930
        self.color = Colors()
        self.surface = Surface(self.screen_size, self.screen_size)
        self.font = Font()

    def starting_window_creation(self) -> None:
        """
            Show the start of the game scene
        """
        self.surface.DISPLAYSURF.fill(self.color.black)
        pygame.display.set_caption("PACMAN")


class Colors:
    def __init__(self) -> None:
        """
            The variables of the colors used in the program
        """
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)


class Surface:
    def __init__(self, screen_size_width: int, screen_size_height: int) -> None:
        """
            Create a surface of the given size
        @args:
            (screen_height, screen_width) [int, int]-the screen sizes
        """
        self.screen_size_width = screen_size_width
        self.screen_size_height = screen_size_height
        self.DISPLAYSURF = pygame.display.set_mode((self.screen_size_width, self.screen_size_height))


class Font:
    def __init__(self) -> None:
        """
            The variables of fonts used in the program
        """
        self.font_size = 60
        self.font_size_small = 20
        self.font = pygame.font.SysFont("Verdana", self.font_size)
        self.font_small = pygame.font.SysFont("Verdana", self.font_size_small)


class GameScene:
    def __init__(self) -> None:
        self.screen = Screen()
        self.score = Score()
        self.time = GameTime()
        self.dots = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.every_sprites = pygame.sprite.Group()

    def game_scene(self, game_time: float) -> None:
        """
            Show the game scene
        @args:
            game_time [float]-the remaining game time
        """
        self.game_time = game_time
        self.score.score = self.score.score_increase(Game_Run.game_scene.dots, Game_Run.pacman_dot_collision_list)
        self.screen.surface.DISPLAYSURF.fill(self.screen.color.black)
        self.current_score = self.screen.font.font_small.render(str(self.score.score), True, self.screen.color.white)
        self.current_time = self.screen.font.font_small.render(str(self.game_time), True, self.screen.color.white)
        self.screen.surface.DISPLAYSURF.blit(self.current_score, (self.score.score_pos, self.score.score_pos))
        self.screen.surface.DISPLAYSURF.blit(self.current_time, (self.time.time_pos_x, self.time.time_pos_y))


class GameOverScene:
    def __init__(self) -> None:
        self.screen = Screen()
        self.game_over_pos_x = 320
        self.game_over_pos_y = 500

        self.game_over = self.screen.font.font.render("Game Over", True, self.screen.color.yellow)

    def game_over_scene(self) -> None:
        """
            Show the game over scene
        """
        self.screen.surface.DISPLAYSURF.fill(self.screen.color.black)
        self.screen.surface.DISPLAYSURF.blit(self.game_over, (self.game_over_pos_x, self.game_over_pos_y))


class SpriteDraw:
    def __init__(self) -> None:
        self.screen = Screen()

    def sprite_draw(self, any_sprite: pygame.sprite.Group) -> None:
        """
            Display a group on the screen
        @args:
            any_sprite [pygame.sprite.Group]- group to be displayed
        """
        self.any_sprite = any_sprite
        self.any_sprite.draw(self.screen.surface.DISPLAYSURF)


class Score:
    def __init__(self) -> None:
        self.score_pos = 20
        self.score = 0

    def score_increase(self, sprite_group: pygame.sprite.Group, hit_list: list) -> int:
        """
            Increase the score
        @args:
            any_sprite [pygame.sprite.Group] - group that is worth points
            hit_list [list] - list containing the sprites the player picked up
        @return:
            self.score [int] - actual score
        """
        self.sprite_group = sprite_group
        self.hit_list = hit_list

        for self.sprite_group in self.hit_list:
            self.score += 1
        return self.score


class GameTime:
    def __init__(self) -> None:
        self.time_pos_x = 930
        self.time_pos_y = 20
        self.max_time = 60000

    def game_time_counting(self) -> float:
        """
            Sets the remaining game time
        @return:
            game_time [float]-the remaining game time
        """
        self.game_time = round(((self.max_time - pygame.time.get_ticks()) / 1000), 2)
        return self.game_time


class Collide:

    def sprite_group_collision(self, sprite: pygame.sprite.Sprite, group: pygame.sprite.Group, kill: bool) -> list:
        """
            Create a list of sprites from the group that collide with the another sprite
        @args:
            sprite [pygame.sprite.Sprite] - the sprite to be tested for collision
            group [pygame.sprite.Group] - the group to be tested for collision
            kill [bool] - remove or not remove from the group
        @return:
            hit_list [list] - list containing the sprites that collided with the other sprite
        """
        self.sprite = sprite
        self.group = group
        self.kill = kill
        hit_list = pygame.sprite.spritecollide(self.sprite, self.group, self.kill)
        return hit_list


class ListToBool:

    def list_checker(self, hit_list: list) -> bool:
        """
            Check if the list has elements
        @args:
            hit_list [list] - the list to be checked
        @return:
            True [bool] - if the list has elements
            False [bool] - if the list has no element
        """
        self.hit_list = hit_list
        if len(self.hit_list) > 0:
            return True
        else:
            return False


class InnerWall:
    def __init__(self) -> None:
        self.pos_list = ((150, 100), (150, 200), (550, 200), (850, 100), (100, 700), (250, 700), (600, 700), (750, 700))
        self.size_list = ((10, 200), (300, 10), (300, 10), (10, 200), (300, 10), (10, 200), (300, 10), (10, 200))
        self.wall = CreateWall()

    def create_wall(self):
        """
            Create the inner walls based on the lists of positions and dimensions by calling the create_wall function
        """
        self.wall.create_wall(self.pos_list, self.size_list, Game_Run.game_scene.walls,
                              Game_Run.game_scene.every_sprites)


class BorderWall:
    def __init__(self) -> None:
        self.pos_list = (
        (0, 0), (0, 0), (0, 990), (990, 0), (0, 550), (990, 550), (550, 0), (550, 990), (0, 450), (0, 550), (890, 450),
        (890, 550), (450, 0), (550, 0), (450, 890), (550, 890))
        self.size_list = (
        (10, 450), (450, 10), (450, 10), (10, 450), (10, 450), (10, 450), (450, 10), (450, 10), (100, 10), (100, 10),
        (110, 10), (100, 10), (10, 100), (10, 100), (10, 110), (10, 100))
        self.wall = CreateWall()

    def create_wall(self):
        """
            Create the border walls based on the lists of positions and dimensions by calling the create_wall function
        """
        self.wall.create_wall(self.pos_list, self.size_list, Game_Run.game_scene.walls,
                              Game_Run.game_scene.every_sprites)


class CreateWall:
    def create_wall(self, list_pos: tuple, list_size: tuple, wall_group: pygame.sprite.Group,
                    every_group: pygame.sprite.Group) -> None:
        """
            Create walls based on the tuples of positions and dimensions and added to the groups
        @args:
            list_pos [tuple] - tuple of wall positions
            list_size [tuple] - tuple of wall sizes
            wall_group [pygame.sprite.Group] - the group of walls
            every_group [pygame.sprite.Group] - the group of all sprites
        """
        self.list_pos = list_pos
        self.list_size = list_size
        self.wall_group = wall_group
        self.every_group = every_group
        for i in range(len(self.list_pos)):
            self.wall_pos_x = self.list_pos[i][0]
            self.wall_pos_y = self.list_pos[i][1]

            self.wall_size_width = self.list_size[i][0]
            self.wall_size_height = self.list_size[i][1]
            self.walls = Wall(self.wall_pos_x, self.wall_pos_y, self.wall_size_width, self.wall_size_height)

            self.wall_group.add(self.walls)
            self.every_group.add(self.walls)


class MapCreation:
    def __init__(self) -> None:
        self.inner_wall = InnerWall()
        self.border = BorderWall()
        self.dot = DotCreation()
        self.screen = Screen()
        self.game = Game()

    def starting_map(self) -> None:
        """
            Create the starting map
        """
        self.screen.starting_window_creation()
        self.border.create_wall()
        self.inner_wall.create_wall()
        self.dot.dot_creation()


class Game:
    def __init__(self) -> None:
        self.game_scene = GameScene()
        self.pacman = PacMan()
        self.move = Move()
        self.draw = SpriteDraw()
        self.pacman_wall_collision_list = self.pacman.collide.sprite_group_collision(self.pacman, self.game_scene.walls,
                                                                                     False)
        self.pacman_wall_collision = self.pacman.bool.list_checker(self.pacman_wall_collision_list)
        self.pacman_dot_collision_list = self.pacman.collide.sprite_group_collision(self.pacman, self.game_scene.dots,
                                                                                    True)
        self.game_scene.every_sprites.add(self.pacman)

    def run(self) -> None:
        """
            Call the functions needed to run the game
        """
        self.game_time = self.game_scene.time.game_time_counting()
        self.game_scene.game_scene(self.game_time)
        self.move.move(self.pacman, self.game_scene.screen.screen_size, self.game_scene.screen.screen_size)
        self.pacman_wall_collision_list = self.pacman.collide.sprite_group_collision(self.pacman, self.game_scene.walls,
                                                                                     False)
        self.pacman_wall_collision = self.pacman.bool.list_checker(self.pacman_wall_collision_list)
        self.pacman_dot_collision_list = self.pacman.collide.sprite_group_collision(self.pacman, self.game_scene.dots,
                                                                                    True)
        self.draw.sprite_draw(self.game_scene.every_sprites)


class IsItOver:
    def __init__(self) -> None:
        self.game_over_scene = GameOverScene()

    def is_it_over(self, score: int, dot_number: int, game_time: float, collision: bool) -> bool:
        """
            Checks if the game is not over
        """
        self.score = score
        self.dot_number = dot_number
        self.time = game_time
        self.collision = collision

        if self.score == self.dot_number or self.time <= 0 or self.collision == True:
            return True
        else:
            return False


class GameOver:
    def __init__(self) -> None:
        self.over = IsItOver()

    def game_over(self):
        self.is_it_over = self.over.is_it_over(Game_Run.game_scene.score.score, Starting_Map.dot.dot_number,
                                               Game_Run.game_time, Game_Run.pacman_wall_collision)
        if self.is_it_over == True:
            time.sleep(0.5)
            self.over.game_over_scene.game_over_scene()
            pygame.display.update()
            for entity in Game_Run.game_scene.every_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    Starting_Map = MapCreation()
    Game_Run = Game()
    Over = GameOver()

    Starting_Map.starting_map()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Game_Run.run()
        Over.game_over()

        pygame.display.update()
        FramePerSec.tick(FPS)
