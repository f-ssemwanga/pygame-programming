#pygame template
import pygame
import random

WIDTH, HEIGHT, FPS = (260, 480, 30) # game window and fps parameters

# colours
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialise common objects
pygame.init()
pygame.mixer.init() # required for sound

#Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() #handles speed


#game loop
running = True
while running:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  #update
  
  #draw / render
  screen.fill(BLACK)
  pygame.display.flip()
  
pygame.quit()
  