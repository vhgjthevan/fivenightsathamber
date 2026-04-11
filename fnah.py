import pygame
import time
import random

# initialization
pygame.init()
pygame.display.set_icon(pygame.image.load('Resources/placeholders/fnah_logo.png'))
# screen = pygame.display.set_mode((1280, 720)) # screen size — can be edited, prob use variables later
screen = pygame.display.set_mode((1280, 720))
# storing the screen's dimensions in variables
scheight = screen.get_height()
scwidth = screen.get_width()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Five Nights at Hamber')
camview = False

# images (idk a better way to do this)
playerroom = pygame.image.load('Resources/placeholders/room0.png')
room = pygame.transform.smoothscale(pygame.image.load('Resources/photos/hambcaf.JPG'), (500, 375))

# while loop for the game
# all this happens when running is TRUE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hkey dont know how it works but it ends the game
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if camview:
                    camview = False
                else:
                    camview = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_mode(pygame.FULLSCREEN)

    keyis = pygame.key.get_pressed() # defines keyis (key is pressed) (can be anything thats just the name i gave to the variable)
    # placeholder image test
    # press keys to switch 'rooms'
    if keyis[pygame.K_0]:
        room = pygame.image.load('Resources/photos/hambcaf.JPG')
    if keyis[pygame.K_1]:
        room = pygame.image.load('Resources/photos/hambclass.JPG')
    if keyis[pygame.K_2]:
        room = pygame.image.load('Resources/photos/hambhallway.JPG')
    if keyis[pygame.K_3]:
        room = pygame.image.load('Resources/photos/hambgym.JPG')
    if keyis[pygame.K_4]:
        room = pygame.image.load('Resources/photos/hambhuddle.JPG')
    if keyis[pygame.K_5]:
        room = pygame.image.load('Resources/photos/hamblibrary.JPG')
    if keyis[pygame.K_6]:
        room = pygame.image.load('Resources/photos/hambmath.JPG')
    if keyis[pygame.K_7]:
        room = pygame.image.load('Resources/photos/hambsci.JPG')
    if keyis[pygame.K_8]:
        room = pygame.image.load('Resources/photos/hambsideent.JPG')
    if keyis[pygame.K_9]:
        room = pygame.image.load('Resources/photos/hambstairs.JPG')
    if keyis[pygame.K_MINUS]:
        room = pygame.image.load('Resources/placeholders/room10.png')
    if keyis[pygame.K_EQUALS]:
        room = pygame.image.load('Resources/placeholders/room11.png')
    if keyis[pygame.K_ESCAPE]:
        running = False

    screen.blit(playerroom, (0,0)) # currently this image is 1280x720, same as the proportions i put in screen size

    # camera window - wip
    if camview:
        screen.blit(pygame.transform.smoothscale(room, (700, 525)), (scwidth-700, 0))
    else:
        screen.blit(pygame.image.load('Resources/placeholders/cameraicon.png'), (scwidth-75, 75))


    pygame.display.flip()
    dt = clock.tick(60) / 1000 # this does something i think

