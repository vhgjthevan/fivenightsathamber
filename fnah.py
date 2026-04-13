import pygame
import time
import random
import determinerooms as detrooms

# initialization
pygame.init()
pygame.display.set_icon(pygame.image.load('Resources/placeholders/fnah_logo.png'))
# screen = pygame.display.set_mode((1280, 720)) # screen size — can be edited, prob use variables later
screen = pygame.display.set_mode((1280, 720))
# storing the screen's dimensions in variables
scheight = screen.get_height()
scwidth = screen.get_width()
clock = pygame.time.Clock()

# misc
running = True
pygame.display.set_caption('Five Nights at Hamber')
camview = False
panspeed = 500

# images (idk a better way to do this)
room = pygame.transform.smoothscale(pygame.image.load('Resources/photos/hambcaf.JPG'), (500, 375))
roombottom = pygame.image.load('Resources/placeholders/securityofficebottom.png')
roommiddle = pygame.image.load('Resources/placeholders/securityofficemiddle.png')
roomtop = pygame.image.load('Resources/placeholders/securityofficetop.png')
camdown = pygame.image.load('Resources/placeholders/cameradown.png')
camup = pygame.image.load('Resources/placeholders/cameraup.png')

margin = (roomtop.get_width() - scwidth) / 2
imagepan = 0

# while loop for the game
# all this happens when running is TRUE
while running:
    mouseis = pygame.mouse.get_pressed()[0]
    camstatus = False
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # hkey dont know how it works but it ends the game
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx in range(scwidth-75, scwidth) and my in range(75, 75+250):
                if camview:
                    camview = False
                else:
                    camview = True

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
        running = False # esc to quit

    screen.blit(roombottom, (imagepan, 0)) # room has three layers, so we can place enemy sprites in between bottom and middle
    screen.blit(roommiddle, (imagepan, 0))
    screen.blit(roomtop, (imagepan, 0))
    camhb = pygame.Rect(scwidth-75, 75, camup.get_width(), camup.get_height()) # camera button hitbox

    # uses transform.smoothscale to anti-alias the image when it scales it down (makes it look less pixelated)
    if camview:
        screen.blit(pygame.transform.smoothscale(room, (700, 525)), (scwidth-700-75, 0)) # first tuple contains the calculated w/h of the scaled image, second tuple subracts image width and camera icon width from screen width for the x, and 0 for the y
        screen.blit(camup, (scwidth-75, 75))
    else:
        screen.blit(camdown, (scwidth-75, 75))

    if imagepan <= -399:
        camstatus = True
    else:
        camstatus = False
    # pan
    mx, my = pygame.mouse.get_pos()
    if camview == False:
        if mx < 150:
            imagepan += panspeed * dt
        if mx > (scwidth-150):
            imagepan -= panspeed * dt
        if imagepan < -margin * 2:
            imagepan = -margin * 2
        if imagepan > 0:
            imagepan = 0
    


    pygame.display.flip()

pygame.quit()
