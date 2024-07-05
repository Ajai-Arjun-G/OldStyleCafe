import pygame
from sys import exit

pygame.init()
text = pygame.font.Font(None,40)

displaySize = (1300,800)
screen = pygame.display.set_mode(displaySize,pygame.RESIZABLE)
pygame.display.set_caption('Lemomade Stand!')

#Background - Basic Colour
surface = pygame.Surface(displaySize)
surface.fill('#87CEEB')

#Clouds in the Background - Layer 2
cloudSurface = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud.png').convert_alpha()

#Resized Cloud - to improve appearance in the background 
cloudSurface = pygame.transform. smoothscale(cloudSurface,(100,90))

#Sun in the Background - Layer 1
sunSurface = pygame.image.load('D:/Term - 4/Pygame/Sun/sun_copy.png').convert_alpha()

#Resized Sun - to improve appearance in the background
sunSurface = pygame.transform.smoothscale(sunSurface,(110,110))

#Furniture in the Background - Layer 3
tableSurface = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen.png').convert_alpha()

#Furniture in the Background - Layer 3
tableSurface2 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - colour.png').convert_alpha()

#Furniture in the Background - Layer 3
tableSurface3 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - colour.png').convert_alpha()

#Furniture in the Background - Layer 3
tableSurface4 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - colour.png').convert_alpha()

#Furniture in the Background - Layer 3
tableSurface5 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - colour.png').convert_alpha()

#Resizing images
tableSurface = pygame.transform.smoothscale(tableSurface,(500,400))

#Furniture - on top of table - Layer 4
coffeemaker = pygame.image.load('D:/Term - 4/Pygame/furniture/coffee-maker_copy.png').convert_alpha()

coffeemaker = pygame.transform.smoothscale(coffeemaker,(130,140))

#Furniture - on top of the table - Layer 4
shelf = pygame.image.load('D:/Term - 4/Pygame/furniture/shelf_copy.png').convert_alpha()

shelf = pygame.transform.smoothscale(shelf,(150,85))

#Furniture - on top of the table - Layer 4
toaster = pygame.image.load('D:/Term - 4/Pygame/furniture/toast_copy.png').convert_alpha()

toaster = pygame.transform.smoothscale(toaster,(100,95))

#People
man1 = pygame.image.load('D:/Term - 4/Pygame/People/grandfather_copy.png').convert_alpha()

man1 = pygame.transform.smoothscale(man1,(270,270))


#Text - just for testing 
text_surface = text.render('Good Day!',False,'Black')


#Rectange of Tables
table1_rect = tableSurface.get_rect(midleft = (0,600))
table2_rect = tableSurface2.get_rect(midleft = (480,685))
table3_rect = tableSurface3.get_rect(midleft = (680,685))
table4_rect = tableSurface4.get_rect(midleft = (880,685))
table5_rect = tableSurface5.get_rect(midleft = (1085,685))

#Rectangle for Sun
sun_rect = sunSurface.get_rect(center = (400,80))

#Rectangle for Cloud
cloud_rect = cloudSurface.get_rect(center = (600,110))

#Rectangle for Furniture on top
shelf_rect = shelf.get_rect(midbottom = (1190,600))

#Rectangle for Coffee Maker
coffeeM_rect = coffeemaker.get_rect(midbottom = (400,600))

#Rectangle for toaster
toaster_rect = toaster.get_rect(midbottom = (550,602))

#Rectange for people
man_rect = man1.get_rect(midbottom = (850,603))

#Frames per second variable
clock = pygame.time.Clock()

#Main loop - to keep the game running
while True:

    #Event checking & ahndling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            displaySize = event.size
            screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
            surface = pygame.Surface(displaySize)
            surface.fill('#87CEEB')
            text_surface = text.render('Good Day!',False,'Black')

    screen.blit(surface,(0,0))

    screen.blit(sunSurface,sun_rect)

    screen.blit(cloudSurface,cloud_rect)

    screen.blit(man1,man_rect)

    screen.blit(tableSurface,table1_rect)
    screen.blit(tableSurface2,table2_rect)
    screen.blit(tableSurface3,table3_rect)
    screen.blit(tableSurface4,table4_rect)
    screen.blit(tableSurface5,table5_rect)

    screen.blit(shelf,shelf_rect)
    screen.blit(coffeemaker,coffeeM_rect)
    screen.blit(toaster,toaster_rect)

    sun_rect.centerx -= 1
    if sun_rect.right <= 0: sun_rect.centerx = 1500

    cloud_rect.centerx -= 2
    if cloud_rect.right <= 0: cloud_rect.x = 1400

    pygame.display.update() # Keep updating the screen
    clock.tick(60)