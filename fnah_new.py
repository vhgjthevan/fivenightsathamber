import pygame

def camchangechecker(camview, camviewhelper):
    if camview == camviewhelper:
        return False
    else:
        return True

pygame.init()
pygame.display.set_icon(pygame.image.load('Resources/placeholders/fnah_logo.png'))
screen = pygame.display.set_mode((1280, 720))
scheight = screen.get_height()
scwidth = screen.get_width()
clock = pygame.time.Clock()
mouseis = pygame.mouse.get_pressed()[0]
mode = 'game'

running = True
pygame.display.set_caption('Five Nights at Hamber')
camview = False
camviewhelper = False
panspeed = 500

viewroom = pygame.transform.smoothscale(pygame.image.load('Resources/photos/hambclass.JPG'), (500, 375))
camroombottom = pygame.image.load('Resources/placeholders/securityofficebottom.png')
camroommiddle = pygame.image.load('Resources/placeholders/securityofficemiddle.png')
camroomtop = pygame.image.load('Resources/placeholders/securityofficetop.png')
camdown = pygame.image.load('Resources/placeholders/cameradown.png')
camup = pygame.image.load('Resources/placeholders/cameraup.png')

margin = (camroomtop.get_width() - scwidth) / 2
imagepan = -margin

screen.blit(camroombottom, (imagepan, 0))
screen.blit(camroommiddle, (imagepan, 0))
screen.blit(camroomtop, (imagepan, 0))

while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if mode == 'game':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx in range(scwidth-75, scwidth) and my in range(75, 75+250):
                    if camview:
                        camview = False
                    else:
                        camview = True
                    if imagepan > -margin*2:
                        camview = False

        if event.type == pygame.KEYUP:
            if camview and mode == "game":
                if event.key == pygame.K_0:
                    viewroom = pygame.image.load('Resources/photos/hambcaf.JPG')
                if event.key == pygame.K_1:
                    viewroom = pygame.image.load('Resources/photos/hambclass.JPG')
                if event.key == pygame.K_2:
                    viewroom = pygame.image.load('Resources/photos/hambhallway.JPG')
                if event.key == pygame.K_3:
                    viewroom = pygame.image.load('Resources/photos/hambgym.JPG')
                if event.key == pygame.K_4:
                    viewroom = pygame.image.load('Resources/photos/hambhuddle.JPG')
                if event.key == pygame.K_5:
                    viewroom = pygame.image.load('Resources/photos/hamblibrary.JPG')
                if event.key == pygame.K_6:
                    viewroom = pygame.image.load('Resources/photos/hambmath.JPG')
                if event.key == pygame.K_7:
                    viewroom = pygame.image.load('Resources/photos/hambsci.JPG')
                if event.key == pygame.K_8:
                    viewroom = pygame.image.load('Resources/photos/hambsideent.JPG')
                if event.key == pygame.K_9:
                    viewroom = pygame.image.load('Resources/photos/hambstairs.JPG')
                if event.key == pygame.K_MINUS:
                    viewroom = pygame.image.load('Resources/placeholders/room10.png')
                if event.key == pygame.K_EQUALS:
                    viewroom = pygame.image.load('Resources/placeholders/room11.png')
            if event.key == pygame.K_ESCAPE:
                if camview:
                    camview = False #quits camview first
                else:
                    running = False # esc to quit
    if mode == "game":
        #panning
        if camview == False:
            mx, my = pygame.mouse.get_pos()
            if mx<150:
                imagepan += panspeed*dt
                panning = True
            elif mx>(scwidth-150):
                imagepan -= panspeed*dt
                panning = True
            else:
                panning=False
            if imagepan < -margin*2:
                imagepan = -margin*2
            if imagepan > 0:
                imagepan = 0

        #only resets the main room if the screen has changed
        if panning:
            screen.blit(camroombottom, (imagepan, 0)) # room has three layers, enemies will be placed on the middle layer.
            screen.blit(camroommiddle, (imagepan, 0))
            screen.blit(camroomtop, (imagepan, 0))
        if camview:
            screen.blit(pygame.transform.smoothscale(viewroom, (700, 525)), (scwidth-700-75, 0)) #first tuple contains the w/h of the scaled img. second tuple subtracts img width and cam icon width from scwidth for the x, and 0 for the y
            screen.blit(camup, (scwidth-75, 75))
        else:
            if imagepan == -margin*2:
                screen.blit(camdown, (scwidth-75, 75))

        #if the viewroom has changed, display new room
        if camchangechecker(camview, camviewhelper):
            camviewhelper = camview
            if camview:
                screen.blit(pygame.transform.smoothscale(viewroom, (700, 525)), (scwidth-700-75, 0))


    if mode == "menu":
        print("MUNU")


    pygame.display.flip()

pygame.quit()
