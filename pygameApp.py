# pygame template
import pygame
import random


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
        self.rect.center = (
            WIDTH / 2,
            HEIGHT,
        )  # position the image in the centre of the screen at the bottom

    def update(self):
        # updates the player object
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


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
