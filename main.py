import pygame
import random
from sys import exit
import math

pygame.init()

displaySize = (1255, 800)
screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
pygame.display.set_caption('Cafe Casablanca!')

# Background - Basic Colour
surface = pygame.Surface(displaySize)
surface.fill('#87CEEB')

# Font
font_path = 'D:/Term - 4/Pygame/font/Margarine/Margarine-Regular.ttf'
font_size = 35
custom_font = pygame.font.Font(font_path, font_size)

# Clouds in the Background - Layer 2
cloudSurface = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud.png').convert_alpha()
cloudSurface2 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-2.png').convert_alpha()
cloudSurface3 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-3.png').convert_alpha()
cloudSurface4 = pygame.image.load('D:/Term - 4/Pygame/Clouds/cloud-4.png').convert_alpha()

# Resized Cloud - to improve appearance in the background
cloudSurface = pygame.transform.smoothscale(cloudSurface, (170, 150))
cloudSurface2 = pygame.transform.smoothscale(cloudSurface2, (170, 150))
cloudSurface3 = pygame.transform.smoothscale(cloudSurface3, (170, 150))
cloudSurface4 = pygame.transform.smoothscale(cloudSurface4, (170, 150))

# Sun in the Background - Layer 1
sunSurface = pygame.image.load('D:/Term - 4/Pygame/Sun/sun_copy.png').convert_alpha()

# Resized Sun - to improve appearance in the background
sunSurface = pygame.transform.smoothscale(sunSurface, (200, 200))

# Furniture in the Background - Layer 3
tableSurface = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen.png').convert_alpha()
tableSurface2 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
tableSurface3 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
tableSurface4 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
tableSurface5 = pygame.image.load('D:/Term - 4/Pygame/furniture/kitchen - copy.png').convert_alpha()
fridge = pygame.image.load('D:/Term - 4/Pygame/furniture/fridge.png').convert_alpha()

fridge = pygame.transform.smoothscale(fridge, (285, 500))
# Resizing images
tableSurface = pygame.transform.smoothscale(tableSurface, (500, 400))

# Furniture - on top of table - Layer 4
coffeemaker = pygame.image.load('D:/Term - 4/Pygame/furniture/coffee-maker.png').convert_alpha()
coffeemaker = pygame.transform.smoothscale(coffeemaker, (250, 250))

# Furniture - on top of the table - Layer 4
toast = pygame.image.load('D:/Term - 4/Pygame/furniture/toast.png').convert_alpha()
toast = pygame.transform.smoothscale(toast, (190, 180))

# Function to load and scale images
def load_and_scale_image(path, size):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(image, size)

# People images paths and sizes
people_images = {
    'men': [
        'D:/Term - 4/Pygame/People/grandfather.png',
        'D:/Term - 4/Pygame/People/grandfather2.png',
        'D:/Term - 4/Pygame/People/old-man.png',
        'D:/Term - 4/Pygame/People/old-man2.png'
    ],
    'women': [
        'D:/Term - 4/Pygame/People/grandmother.png',
        'D:/Term - 4/Pygame/People/grandmother2.png',
        'D:/Term - 4/Pygame/People/great-grandmother.png',
        'D:/Term - 4/Pygame/People/old-woman.png',
        'D:/Term - 4/Pygame/People/old-woman2.png'
    ],
    'children': [
        'D:/Term - 4/Pygame/People/boy.png',
        'D:/Term - 4/Pygame/People/daughter.png'
    ]
}

# Size for all people images
people_size = (370, 370)

# Rectangle for people
person_rect = pygame.Rect(0, 0, 370, 370)
person_rect.midbottom = (780, 900)



# Load and scale all people images
men_images = [load_and_scale_image(path, people_size) for path in people_images['men']]
women_images = [load_and_scale_image(path, people_size) for path in people_images['women']]
children_images = [load_and_scale_image(path, people_size) for path in people_images['children']]

money_tab = pygame.image.load('D:/Term - 4/Pygame/Money/circle.png').convert_alpha()
money_tab = pygame.transform.smoothscale(money_tab, (160, 120))

#Coin adding effect
coin = pygame.image.load('D:/Term - 4/Pygame/Money/dollar.png').convert_alpha()
coin = pygame.transform.smoothscale(coin, (50, 50))

plus = pygame.image.load('D:/Term - 4/Pygame/Money/add.png').convert_alpha()
plus  = pygame.transform.smoothscale(plus, (25, 25))

# Food
bread = pygame.image.load('D:/Term - 4/Pygame/food/toast.png').convert_alpha()
coffee = pygame.image.load('D:/Term - 4/Pygame/food/coffee-cup.png').convert_alpha()

#tool tip with request
requesttoast = pygame.image.load('D:/Term - 4/Pygame/food/toast.png').convert_alpha()
requestcoffee = pygame.image.load('D:/Term - 4/Pygame/food/coffee-cup.png').convert_alpha()

requestcoffee = pygame.transform.smoothscale(requestcoffee,(90,90))
requesttoast = pygame.transform.smoothscale(requesttoast,(110,110))

# Request
request = pygame.image.load('D:/Term - 4/Pygame/People/speech-bubble.png').convert_alpha()
request = pygame.transform.smoothscale(request,(250,250))

# Resize food
bread = pygame.transform.smoothscale(bread, (150, 150))
coffee = pygame.transform.smoothscale(coffee, (120, 130))

#Correct
correct = pygame.image.load('D:/Term - 4/Pygame/food/check-mark.png').convert_alpha()
correct = pygame.transform.smoothscale(correct,(60,60))

#Wrong
wrong = pygame.image.load('D:/Term - 4/Pygame/food/wrong.png').convert_alpha()
wrong = pygame.transform.smoothscale(wrong,(50,50))

#mouse
mouse = pygame.image.load('D:/Term - 4/Pygame/furniture/left-click.png').convert_alpha()
mouse = pygame.transform.smoothscale(mouse,(40,40))

#c key
keyC =  pygame.image.load('D:/Term - 4/Pygame/furniture/letter-c.png').convert_alpha()
keyC = pygame.transform.smoothscale(keyC,(40,40))

#t key
keyT =  pygame.image.load('D:/Term - 4/Pygame/furniture/letter-t.png').convert_alpha()
keyT = pygame.transform.smoothscale(keyT,(40,40))

#slash
slash = pygame.image.load('D:/Term - 4/Pygame/furniture/slash.png').convert_alpha()
slash = pygame.transform.smoothscale(slash,(35,35))

# Rectangle of Tables
table1_rect = tableSurface.get_rect(midleft=(-30, 700))
table2_rect = tableSurface2.get_rect(midleft=(450, 785))
table3_rect = tableSurface3.get_rect(midleft=(650, 785))
table4_rect = tableSurface4.get_rect(midleft=(850, 785))
table5_rect = tableSurface5.get_rect(midleft=(1055, 785))
fridge_rect = fridge.get_rect(midleft=(1255, 685))

# Rectangle for Sun
sun_rect = sunSurface.get_rect(center=(200, 120))

# Rectangle for Cloud
cloud_rect = cloudSurface.get_rect(center=(1600, 130))
cloud2_rect = cloudSurface2.get_rect(center=(1600, 130))
cloud3_rect = cloudSurface3.get_rect(center=(1600, 130))
cloud4_rect = cloudSurface4.get_rect(center=(1600, 130))

# Rectangle for Furniture on top
toaster_rect = toast.get_rect(midbottom=(1100, 710))

# Rectangle for Coffee Maker
coffeeM_rect = coffeemaker.get_rect(midbottom=(400, 700))

# Rectangle for food
bread_rect = bread.get_rect(midbottom=(780, 670))
coffee_rect = coffee.get_rect(midbottom=(780, 670))

# Rectangle for the money_tab
tab_rect = money_tab.get_rect(center=(1150, 90))

# Rectangle for the bank
coin_rect = coin.get_rect(center=(790, 300))

#Rectangle for bubble
req_rect = request.get_rect(midbottom = (1050,400))

#Rectangle for the coffee and bread
reqcof_rect = requestcoffee.get_rect(center = (req_rect.centerx+15,req_rect.centery-10))
reqtost_rect = requesttoast.get_rect(center = (req_rect.centerx+10,req_rect.centery-15))

#Rectangle of add
posPlus = coin_rect.midleft
plus_rect = plus.get_rect(midright = (posPlus[0]-5,posPlus[1]))

#Rectangle for correct
correct_rect = correct.get_rect(midleft = (reqcof_rect.bottomright[0]-35,reqcof_rect.bottomright[1]-10))

#Rectangle for wrong
wrong_rect = wrong.get_rect(midleft = (reqcof_rect.bottomright[0]-35,reqcof_rect.bottomright[1]-10))

#Rectangle for keys
mouse_rect = mouse.get_rect(center = (360,410))
c_rect = keyC.get_rect(center = (435,410))
slash_rect = slash.get_rect(center = (395,410))
mouse_rect2 = mouse.get_rect(center = (1050,490))
t_rect = keyT.get_rect(center = (1125,490))
slash_rect2 = slash.get_rect(center = (1085,490))

# Detect Collision - flag bit
collision_detected = False
bread_flag = False
coffee_flag = False

# People flag bits
person_appeared = False
person_moving = False

# Timer variables
BREAD_DISPLAY_TIME = 2000  # milliseconds
COFFEE_DISPLAY_TIME = 2000  # milliseconds
person_display_time = 5000
person_timer = 0
bread_timer = 0
coffee_timer = 0

# Floating variables
bread_float = 0
coffee_float = 0
person_float = 0

#How much should they move around
float_distance = 3
float_speed = 2

# Score
score = 0

#Wiggling Sun
sunAngle = 0
rotateSunSpeed = 0.1
rotateRange = 5
rotateDirection = 1

# Key timers
keyTimer = 10000

# Frames per second variable
clock = pygame.time.Clock()

# Combine all images into a single dictionary
all_people_images = {
    'men': men_images,
    'women': women_images,
    'children': children_images
}

def randomly_select_person():
    category = random.choice(list(all_people_images.keys()))
    image = random.choice(all_people_images[category])
    return image

def random_select_req():
    return random.choice(['coffee','toast'])

def randomly_select_cloud():
    return random.choice(['cloud1', 'cloud2', 'cloud3', 'cloud4'])

current_person = randomly_select_person()
current_cloud = randomly_select_cloud()

bread_initial_y = bread_rect.centery
coffee_initial_y = coffee_rect.centery

# Add a variable to keep track of the blink state
blink_state = True
blink_interval = 500  # Blink interval in milliseconds
last_blink_time = pygame.time.get_ticks()

# Main loop - to keep the game running
while True:
    current_time = pygame.time.get_ticks()

    # Update the blink state
    if current_time - last_blink_time >= blink_interval:
        blink_state = not blink_state
        last_blink_time = current_time

    bread_float_offset = math.sin(current_time*float_speed/200)*float_distance
    coffee_float_offset = math.sin(current_time*float_speed/200)*float_distance

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            displaySize = event.size
            screen = pygame.display.set_mode(displaySize, pygame.RESIZABLE)
            surface = pygame.Surface(displaySize)
            surface.fill('#87CEEB')
            tab_rect = money_tab.get_rect(center=(displaySize[0] - 105, 90)) 
            screen.blit(money_tab, tab_rect)

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                bread_flag, coffee_flag = True, False
                collision_detected = True
                bread_timer = current_time + BREAD_DISPLAY_TIME
            elif event.key == pygame.K_c:
                coffee_flag, bread_flag = True, False
                collision_detected = True
                coffee_timer = current_time + COFFEE_DISPLAY_TIME

    screen.blit(surface, (0, 0))

    sunAngle += rotateSunSpeed * rotateDirection
    if abs(sunAngle) >= rotateRange:
        rotateDirection *= -1

    # Rotate and blit the sun
    rotated_sun = pygame.transform.rotozoom(sunSurface, sunAngle,1)
    rotated_sun_rect = rotated_sun.get_rect(center=sun_rect.center)
    screen.blit(rotated_sun, rotated_sun_rect)

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
        val = random_select_req()
        person_appeared = True
        person_timer = current_time + person_display_time

    # Display the current person if appeared
    if person_appeared:
        screen.blit(request,req_rect)
        if val == 'toast':
            screen.blit(requesttoast,reqtost_rect)
            target = 'toast'
        else:
            screen.blit(requestcoffee,reqcof_rect)
            target = 'coffee'
        screen.blit(current_person, person_rect)
        if person_rect.midbottom[1] > 715:
            person_rect.centery -= 12

    screen.blit(tableSurface, table1_rect)
    screen.blit(tableSurface2, table2_rect)
    screen.blit(tableSurface3, table3_rect)
    screen.blit(tableSurface4, table4_rect)
    screen.blit(tableSurface5, table5_rect)
    screen.blit(fridge, fridge_rect)

    # Handle bread display and person disappearance
    if bread_flag and target == 'coffee':
        if current_time < bread_timer:
            screen.blit(wrong,wrong_rect)
            bread_rect.centery = bread_initial_y + int(bread_float_offset)
            screen.blit(bread, bread_rect)
    elif bread_flag:
        bread_rect.centery = bread_initial_y + int(bread_float_offset)
        screen.blit(bread, bread_rect)
        if target == 'toast'and coin_rect.centery > 180:
            screen.blit(plus,plus_rect)
            screen.blit(coin,coin_rect)
            coin_rect.centery -= 2
            plus_rect.centery -= 2
        if current_time > bread_timer and target == 'toast':
            person_appeared = False
            bread_flag = False
            score += 2
            coin_rect.centery = 300
            plus_rect.midright = (posPlus[0]-5,posPlus[1])
            person_rect.midbottom = (780,900)
        elif current_time < bread_timer and target == 'toast':
            screen.blit(correct,correct_rect)

    # Handle coffee display and person disappearance
    if coffee_flag and target == 'toast':
        if current_time < coffee_timer:
            screen.blit(wrong,wrong_rect)
            coffee_rect.centery = coffee_initial_y + int(coffee_float_offset)
            screen.blit(coffee, coffee_rect)
    elif coffee_flag:
        coffee_rect.centery = coffee_initial_y + int(coffee_float_offset)
        screen.blit(coffee, coffee_rect)
        if target == 'coffee' and coin_rect.centery > 180:
            screen.blit(plus,plus_rect)
            screen.blit(coin,coin_rect)
            coin_rect.centery -= 2
            plus_rect.centery -= 2
        if current_time > coffee_timer and target == 'coffee':
            person_appeared = False
            coffee_flag = False
            score += 5 
            coin_rect.centery = 300
            plus_rect.midright = (posPlus[0]-5,posPlus[1])
            person_rect.midbottom = (780,900)
        elif current_time < coffee_timer and target == 'coffee':
            screen.blit(correct,correct_rect)

    screen.blit(toast, toaster_rect)
    screen.blit(coffeemaker, coffeeM_rect)

    # Blink the mouse and keys
    if keyTimer > 0:
        if blink_state:
            screen.blit(mouse,mouse_rect)
            screen.blit(mouse,mouse_rect2)
            screen.blit(keyC,c_rect)
            screen.blit(keyT,t_rect)
            screen.blit(slash,slash_rect)
            screen.blit(slash,slash_rect2)
        keyTimer -= 30

    if current_cloud == 'cloud1':
        cloud_rect.centerx -= 2
        if cloud_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud_rect = cloudSurface.get_rect(center=(2000, random.randint(50, 150)))
    elif current_cloud == 'cloud2':
        cloud2_rect.centerx -= 2
        if cloud2_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud2_rect = cloudSurface2.get_rect(center=(2000, random.randint(50, 150)))
    elif current_cloud == 'cloud3':
        cloud3_rect.centerx -= 2
        if cloud3_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud3_rect = cloudSurface3.get_rect(center=(2000, random.randint(50, 150)))
    elif current_cloud == 'cloud4':
        cloud4_rect.centerx -= 2
        if cloud4_rect.right <= 0:
            current_cloud = randomly_select_cloud()
            cloud4_rect = cloudSurface4.get_rect(center=(2000, random.randint(50, 150)))

    screen.blit(money_tab, tab_rect)
    # Display score
    score_text = custom_font.render(f"$ {score}", True, (0, 0, 0))  # Adjust text color as needed
    score_text_rect = score_text.get_rect(center=(tab_rect.centerx, tab_rect.centery-2))
    screen.blit(score_text, score_text_rect)

    pygame.display.update()
    clock.tick(60)
