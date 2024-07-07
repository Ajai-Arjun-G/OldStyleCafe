import pygame
import random
from sys import exit

pygame.init()
text = pygame.font.Font(None,40)

displaySize = (1255,800)
screen = pygame.display.set_mode(displaySize,pygame.RESIZABLE)
pygame.display.set_caption('Cafe Casablanca!')

#Background - Basic Colour
surface = pygame.Surface(displaySize)
surface.fill('#87CEEB')

#Font
font_path = 'D:/Term - 4/Pygame/font\Anton_SC/AntonSC-Regular.ttf'
font_size = 50
custom_font = pygame.font.Font(font_path, font_size)

#Clouds in the Background - Layer 2
cloudSurface = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud.png').convert_alpha()
cloudSurface2 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-2.png').convert_alpha()
cloudSurface3 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-3.png').convert_alpha()
cloudSurface4 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-4.png').convert_alpha()

#Resized Cloud - to improve appearance in the background 
cloudSurface = pygame.transform. smoothscale(cloudSurface,(170,150))
cloudSurface2 = pygame.transform. smoothscale(cloudSurface2,(170,150))
cloudSurface3 = pygame.transform. smoothscale(cloudSurface3,(170,150))
cloudSurface4 = pygame.transform. smoothscale(cloudSurface4,(170,150))

#Sun in the Background - Layer 1
sunSurface = pygame.image.load('D:/Term - 4/Pygame/Sun/sun_copy.png').convert_alpha()

#Resized Sun - to improve appearance in the background
sunSurface = pygame.transform.smoothscale(sunSurface,(200,200))

#Furniture in the Background - Layer 3
tableSurface = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen.png').convert_alpha()
#Furniture in the Background - Layer 3
tableSurface2 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
#Furniture in the Background - Layer 3
tableSurface3 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
#Furniture in the Background - Layer 3
tableSurface4 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
#Furniture in the Background - Layer 3
tableSurface5 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
#Furniture in the Background - Layer 3
fridge = pygame.image.load('D:/Term - 4/Pygame/furniture/fridge.png').convert_alpha()

fridge = pygame.transform.smoothscale(fridge,(285,650))
#Resizing images
tableSurface = pygame.transform.smoothscale(tableSurface,(500,400))

#Furniture - on top of table - Layer 4
coffeemaker = pygame.image.load('D:/Term - 4/Pygame/furniture/coffee-maker.png').convert_alpha()
coffeemaker = pygame.transform.smoothscale(coffeemaker,(250,250))

#Furniture - on top of the table - Layer 4
toast = pygame.image.load('D:/Term - 4/Pygame/furniture/toast.png').convert_alpha()
toast = pygame.transform.smoothscale(toast,(190,180))

#People
man1 = pygame.image.load('D:/Term - 4/Pygame/People/grandfather.png').convert_alpha()
man1 = pygame.transform.smoothscale(man1,(370,370))
fem1 = pygame.image.load('D:/Term - 4/Pygame/People/grandmother.png').convert_alpha()
fem1 = pygame.transform.smoothscale(fem1,(370,370))


#Food
bread = pygame.image.load('D:/Term - 4/Pygame/food/toast.png').convert_alpha()
coffee = pygame.image.load('D:/Term - 4/Pygame/food/coffee-cup.png').convert_alpha()

#Resize food
bread = pygame.transform.smoothscale(bread,(150,150))
coffee = pygame.transform.smoothscale(coffee,(120,130))

#Rectange of Tables
table1_rect = tableSurface.get_rect(midleft = (-30,700))
table2_rect = tableSurface2.get_rect(midleft = (450,785))
table3_rect = tableSurface3.get_rect(midleft = (650,785))
table4_rect = tableSurface4.get_rect(midleft = (850,785))
table5_rect = tableSurface5.get_rect(midleft = (1055,785))
fridge_rect = fridge.get_rect(midleft = (1255,685))

#Rectangle for Sun
sun_rect = sunSurface.get_rect(center = (200,120))

#Rectangle for Cloud
cloud_rect = cloudSurface.get_rect(center = (1400,130))
cloud2_rect = cloudSurface2.get_rect(center = (1400,130))
cloud3_rect = cloudSurface3.get_rect(center = (1400,130))
cloud4_rect = cloudSurface4.get_rect(center = (1400,130))

#Rectangle for Furniture on top
toaster_rect = toast.get_rect(midbottom = (1100,710))

#Rectangle for Coffee Maker
coffeeM_rect = coffeemaker.get_rect(midbottom = (400,700))

#Rectange for people
man_rect = man1.get_rect(midbottom = (780,707))
fem_rect = fem1.get_rect(midbottom = (780,703))

#rectangole for food
bread_rect = bread.get_rect(midbottom = (850,600))
coffee_rect = coffee.get_rect(midbottom = (850,600))

#Detect Collision - flag bit
collision_detected = False
bread_flag = False
coffee_flag = False

#People flag bits
person_appeared = False

# Timer variables
BREAD_DISPLAY_TIME = 2000  # milliseconds
COFFEE_DISPLAY_TIME = 2000  # milliseconds
person_display_time = 5000
person_timer = 0
bread_timer = 0
coffee_timer = 0

#Frames per second variable
clock = pygame.time.Clock()

def randomly_select_person():
    return random.choice(['man', 'woman'])

def randomly_select_cloud():
    return random.choice(['cloud1', 'cloud2','cloud3','cloud4'])

current_person = randomly_select_person()
current_cloud = randomly_select_cloud()

#Main loop - to keep the game running
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            displaySize = event.size
            screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
            surface = pygame.Surface(displaySize)
            surface.fill('#87CEEB')
            
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if toaster_rect.collidepoint((event.pos)) and not collision_detected:
                bread_flag, coffee_flag = True, False
                collision_detected = True
                bread_timer = current_time + BREAD_DISPLAY_TIME
            elif coffeeM_rect.collidepoint((event.pos)) and not collision_detected:
                coffee_flag, bread_flag = True, False
                collision_detected = True
                coffee_timer = current_time + COFFEE_DISPLAY_TIME
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Reset collision detection flag on mouse button release
                collision_detected = False

    screen.blit(surface, (0, 0))
    screen.blit(sunSurface, sun_rect)

    if current_cloud == 'cloud1':
        screen.blit(cloudSurface, cloud_rect)
    elif current_cloud == 'cloud2':
        screen.blit(cloudSurface2, cloud2_rect)
    elif current_cloud == 'cloud3':
        screen.blit(cloudSurface3, cloud3_rect)
    else:
        screen.blit(cloudSurface4, cloud4_rect)
    

    # Check if it's time for a new person to appear
    if current_time >= person_timer and not person_appeared:
        current_person = randomly_select_person()
        person_appeared = True
        person_timer = current_time + person_display_time

    screen.blit(tableSurface, table1_rect)
    screen.blit(tableSurface2, table2_rect)
    screen.blit(tableSurface3, table3_rect)
    screen.blit(tableSurface4, table4_rect)
    screen.blit(tableSurface5, table5_rect)
    screen.blit(fridge, fridge_rect)

    # Display the current person if appeared
    if person_appeared:
        if current_person == 'man':
            screen.blit(man1, man_rect)
        elif current_person == 'woman':
            screen.blit(fem1, fem_rect)

    # Handle bread display and person disappearance
    if bread_flag:
        screen.blit(bread, bread_rect)
        if current_time > bread_timer:
            person_appeared = False
            bread_flag = False

    # Handle coffee display and person disappearance
    if coffee_flag:
        screen.blit(coffee, coffee_rect)
        if current_time > coffee_timer:
            person_appeared = False
            coffee_flag = False

    screen.blit(toast,toaster_rect)
    screen.blit(coffeemaker, coffeeM_rect)

    if current_cloud == 'cloud1':
        cloud_rect.centerx -= 2
        if cloud_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud_rect = cloudSurface.get_rect(center=(1400, random.randint(50, 150)))
    elif current_cloud == 'cloud2':
        cloud2_rect.centerx -= 2
        if cloud2_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud2_rect = cloudSurface2.get_rect(center=(1400, random.randint(50, 150)))
    elif current_cloud == 'cloud3':
        cloud3_rect.centerx -= 2
        if cloud3_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud3_rect = cloudSurface3.get_rect(center=(1400, random.randint(50, 150)))
    if current_cloud == 'cloud4':
        cloud4_rect.centerx -= 2
        if cloud4_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud4_rect = cloudSurface4.get_rect(center=(1400, random.randint(50, 150)))


    pygame.display.update()
    clock.tick(60)
