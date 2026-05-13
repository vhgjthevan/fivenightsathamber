import pygame

def camchangechecker(camview, camviewhelper):
    if camview == camviewhelper:
        return False
    else:
        return True

def blitcamroom():
    screen.blit(camroombottom, (imagepan, 0))
    screen.blit(camroommiddle, (imagepan, 0))
    screen.blit(camroomtop, (imagepan, 0))
    screen.blit(settingscog, (-5, -5))

def settingswindow(settingson):
    if settingson:

        blitmenu()
        print('settings = false')
        settingson = False
    else:
        settingson = True
        screen.blit(settingsbg, (scwidth//3, 0))
        print("blitted settings")

def blitmenu():
    screen.blit(menubkg, (0, 0))
    screen.blit(startbutton, (scwidth//2 - startbutton.get_width() - 25, 575))
    screen.blit(settingsbutton, (scwidth//2 + 25, 575))
    print('menu blit')

    #blit the settings menu over the screen
    #make buttons visible and pressable
    #able to be closed


#when given an object, and an x y pos, checks if the mouse is within the bounds
def inbounds(obj, xmin, ymin):
    if mx in range(xmin, xmin + obj.get_width()) and my in range(ymin, ymin + obj.get_height()):
        return True
    else:
        return False

pygame.init()
pygame.display.set_icon(pygame.image.load('Resources/placeholders/fnah_logo.png'))
screen = pygame.display.set_mode((1280, 720))
scheight = screen.get_height()
scwidth = screen.get_width()
clock = pygame.time.Clock()
mouseis = pygame.mouse.get_pressed()[0]
mode = 'menu'
menubkg = pygame.image.load('Resources/fnaftitlescreen.png')

running = True
pygame.display.set_caption('Five Nights at Hamber')
camview = False
camviewhelper = False
panspeed = 500
settingson = False

viewroom = pygame.transform.smoothscale(pygame.image.load('Resources/photos/hambclass.JPG'), (500, 375))
settingscog = pygame.transform.smoothscale(pygame.image.load('Resources/settingscog.png'), (75, 75))
camroombottom = pygame.image.load('Resources/placeholders/securityofficebottom.png')
camroommiddle = pygame.image.load('Resources/placeholders/securityofficemiddle.png')
camroomtop = pygame.image.load('Resources/placeholders/securityofficetop.png')
camdown = pygame.image.load('Resources/placeholders/cameradown.png')
camup = pygame.image.load('Resources/placeholders/cameraup.png')
startbutton = pygame.image.load('Resources/startbutton.png')
settingsbutton = pygame.image.load('Resources/settingsbutton.png')
settingsbg = pygame.image.load('Resources/settingsbox.png')
slider = pygame.image.load('Resources/volumesliderbar.png')
thumb = pygame.image.load('Resources/volumesliderthumb.png')

margin = (camroomtop.get_width() - scwidth) / 2
imagepan = -margin

blitmenu()


while running:
    dt = clock.tick(60) / 1000
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            '''
        if settingson:
            #volume slider
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inbounds(TBD, x, y):
                    TBD
 '''
        if settingson:
            screen.blit(settingsbg, (scwidth/2 - settingsbg.get_width()/2), (scheight/2 - settingsbg.get_height()/2))
            screen.blit(slider, (scwidth/2 - slider.get_width()/2), (scheight/2 - slider.get_height()/2))


        if mode == 'game':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inbounds(camdown, scwidth-75, 75):
                    if camview:
                        camview = False
                    else:
                        camview = True
                    if imagepan > -margin*2:
                        camview = False
                        (scwidth/2 - startbutton.get_width() - 25, )

                elif inbounds(settingscog, -5, -5):
                    settingswindow()
                    print("triggered settings")


        elif mode == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:

                if inbounds(startbutton, scwidth//2 - startbutton.get_width() - 25, 575):
                    mode = "game"
                    blitcamroom()
                elif inbounds(settingsbutton, scwidth//2 + 25, 575):
                    settingswindow(settingson)
                    print("triggered settings")



        if event.type == pygame.KEYUP:
            if camview and mode == "game":
                if event.key == pygame.K_0:
                    viewroom = pygame.image.load('Resources/photos/hambcaf.JPG')
                elif event.key == pygame.K_1:
                    viewroom = pygame.image.load('Resources/photos/hambclass.JPG')
                elif event.key == pygame.K_2:
                    viewroom = pygame.image.load('Resources/photos/hambhallway.JPG')
                elif event.key == pygame.K_3:
                    viewroom = pygame.image.load('Resources/photos/hambgym.JPG')
                elif event.key == pygame.K_4:
                    viewroom = pygame.image.load('Resources/photos/hambhuddle.JPG')
                elif event.key == pygame.K_5:
                    viewroom = pygame.image.load('Resources/photos/hamblibrary.JPG')
                elif event.key == pygame.K_6:
                    viewroom = pygame.image.load('Resources/photos/hambmath.JPG')
                elif event.key == pygame.K_7:
                    viewroom = pygame.image.load('Resources/photos/hambsci.JPG')
                elif event.key == pygame.K_8:
                    viewroom = pygame.image.load('Resources/photos/hambsideent.JPG')
                elif event.key == pygame.K_9:
                    viewroom = pygame.image.load('Resources/photos/hambstairs.JPG')
                elif event.key == pygame.K_MINUS:
                    viewroom = pygame.image.load('Resources/placeholders/room10.png')
                elif event.key == pygame.K_EQUALS:
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
            blitcamroom()

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






   # elif mode == "menu":

    pygame.display.flip()

pygame.quit()















''' decorational spamtong

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠤⠐⠒⠒⠒⠒⠢⠤⠤⠤⠀⠄⠲⠀
⠀⠀⠀⠀⠰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠚⢲⠀
⠀⠀⠀⠀⠀⠁⠀⠿⠿⡿⠿⠿⢿⣶⡀⠀⠰⠋⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⡇⢸⣿⣿⡇⣙⡃⠠⠈⠁⠀⠀
⠀⠀⠀⠀⠀⣄⡉⢉⣵⣮⣭⡍⠑⣿⣿⡆⠀⠤⠀⠀
⢀⣰⣶⡶⡶⠟⠻⠻⠟⠿⠛⢁⣴⣿⠏⠁⠀⡐⠚⠀
⠀⠀⠀⠀⠀⠈⢿⣇⠹⠉⠹⣾⣿⠏⠀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⠁⢾⣈⣙⣀⣿⡏⠀⠡⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⢤⣤⣤⠄⠀⠀⠀⠰⠀⠀⠀⠀
⠀⣤⣤⠁⢀⠂⡀⠀⠀⠙⠁⠀⠀⠘⢂⠀⠁⡄⠀⠀
⠈⠙⠛⠈⠀⠀⢡⠀⠀⠀⠀⠀⢸⠀⠀⠰⢈⣿⣶⠀
⠀⠀⠀⠀⠀⠀⠀⠰⣠⡤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⠟⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


'''
