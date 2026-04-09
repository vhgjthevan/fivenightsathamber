import pygame
import time
import random

# initialization
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # screen size — can be edited, prob use variables later
# storing the screen's dimensions in variables
scheight = screen.get_height()
scwidth = screen.get_width()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Five Nights at Hamber')

# images (idk a better way to do this)
room = pygame.image.load('Resources/room0.png')

# while loop for the game
# all this happens when running is TRUE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hkey dont know how it works but it ends the game
            running = False

    keyis = pygame.key.get_pressed() # defines keyis (key is pressed) (can be anything thats just the name i gave to the variable)
    # placeholder image test
    # press keys to switch 'rooms'
    if keyis[pygame.K_0]:
        room = pygame.image.load('Resources/room0.png')
    if keyis[pygame.K_1]:
        room = pygame.image.load('Resources/room1.png')
    if keyis[pygame.K_2]:
        room = pygame.image.load('Resources/room2.png')
    if keyis[pygame.K_3]:
        room = pygame.image.load('Resources/room3.png')
    if keyis[pygame.K_4]:
        room = pygame.image.load('Resources/room4.png')
    if keyis[pygame.K_5]:
        room = pygame.image.load('Resources/room5.png')
    if keyis[pygame.K_6]:
        room = pygame.image.load('Resources/room6.png')
    if keyis[pygame.K_7]:
        room = pygame.image.load('Resources/room7.png')
    if keyis[pygame.K_8]:
        room = pygame.image.load('Resources/room8.png')
    if keyis[pygame.K_9]:
        room = pygame.image.load('Resources/room9.png')
    if keyis[pygame.K_MINUS]:
        room = pygame.image.load('Resources/room10.png')
    if keyis[pygame.K_EQUALS]:
        room = pygame.image.load('Resources/room11.png')
    if keyis[pygame.K_SPACE]:
		if camview:
			camview = False
		else:
			camview = True

    screen.blit(room, (0,0)) # currently this image is 1280x720, same as the proportions i put in screen size

    # camera window - wip
    if camview:
        pygame.draw.rect(screen, (89, 78, 65), (room.get_width()-10, room.get_height()-10, room.get_width()+20, room.get_height()+20))

    pygame.display.flip()
    dt = clock.tick(60) / 1000 # this does something i think

