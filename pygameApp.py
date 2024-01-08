# pygame template
import pygame
import random

from pygame.sprite import _Group


WIDTH, HEIGHT, FPS = (800, 600, 30)  # game window and fps parameters

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialise common objects
pygame.init()
pygame.mixer.init()  # required for sound


# create a player class which is a type of sprite
class Player(pygame.sprite.Sprite):
    # player class from a sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        # create a rect bounding box
        self.rect = self.image.get_rect()
        # position the image in the centre of the screen at the bottom
        self.rect.center = (
            WIDTH / 2,
            HEIGHT,
        )
        self.rect.bottom = HEIGHT - 10

        # add a speed variable
        self.speedx = 0

    def update(self):
        # updates the player object
        # set player's starting position
        if self.rect.left > WIDTH:
            self.rect.right = 0
        # update position of the player using key events
        self.speedx = 0
        keystate = pygame.key.get_pressed()  # returns a list of keys that are down
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx  # move the box by the speed value

        # add constraints
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    # enemy object class
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        # spawn image at the top of the screen
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy

        # destroy enemy when they get to the bottom of the screen
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # handles speed

# create a sprites group
all_sprites = pygame.sprite.Group()

# create a player object and add it to the sprites group
player = Player()
all_sprites.add(player)
# game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()
    # draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
