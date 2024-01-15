# pygame template
import pygame
import random

from os import path

img_dir = path.join(path.dirname(__file__), "img")
WIDTH, HEIGHT, FPS = (800, 600, 30)  # game window and fps parameters

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialise common objects
pygame.init()
pygame.mixer.init()  # required for sound


# create a player class which is a type of sprite
class Player(pygame.sprite.Sprite):
    # player class from a sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(GREEN)
        self.image = pygame.transform.scale(player_img, (50,38))
        self.image.set_colorkey(BLACK) # removes background
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

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


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


class Bullet(pygame.sprite.Sprite):
    # bullet class
    def __init__(self, x, y):
        # x,y are re-spawn position based on the bullet
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

        # set re-spawn pos to be in front of the player
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        # rect moves upwards
        self.rect.y += self.speedy
        # kill it if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # handles speed
# load all game graphics
background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
background_rect = background.get_rect()

#load other images to the game
player_img = pygame.image.load(path.join(img_dir, "spaceShip.png")).convert()

# create a sprites group
all_sprites = pygame.sprite.Group()

# create an enemy sprites group
mobs = pygame.sprite.Group()

# create a bullects sprite group
bullets = pygame.sprite.Group()

# spawn an enemy
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


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
        # add a shoot method
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # update
    all_sprites.update()
    # check if bullet hits a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #respawn mobs
    for hit in hits:
        m = Mob()
        mobs.add(m)
        all_sprites.add(m)
    # check for collision
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    # draw / render
    screen.fill(BLACK)
    #draw a background
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
