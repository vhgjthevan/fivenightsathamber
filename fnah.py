import pygame
import time
import random

# initialization
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # screen size — can be edited, prob use variables later
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Five Nights at Hamber')

# images (idk a better way to do this)
room0 = pygame.image.load('Resources/room0.png')

# while loop for the game
# all this happens when running is TRUE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hkey dont know how it works but it ends the game
            running = False

    screen.blit(room0, (0,0)) # currently this image is 1280x720, same as the proportions i put in screen size

    pygame.display.flip()
    dt = clock.tick(60) / 1000 # this does something i think
