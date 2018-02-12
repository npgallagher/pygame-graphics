# Computer Programming 1
# Unit 11 - Graphics
#


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

#Images
'''plane = pygame.image.load('plane.png')'''

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
BRIGHT_YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (128, 128, 128)
BLUE_GREY = (119,136,153)
NIGHT = (5, 5, 5)
PURPLE = (128, 0 , 128)
TEAL = (0, 128, 128)
AQUA = (0, 255, 255)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)
MEDIUM_GREEN = (0, 150, 0)
BLACK = (0, 0, 0)

#Character
loc = [380, 280]
vel = [0,0]
speed = 5


'''def draw_plane():
    a = 100
    b = 200
    p = [a,b]
    screen.blit(plane, (100, 200))'''

''' Make rain '''
rain = []
for i in range(400):
    x = random.randrange(-200, 800)
    y = random.randrange(-50, 600)
    r = random.randrange(1, 2)
    z = random.randrange(1, 8)
    g = random.randrange(450, 600)
    s = [x, y, r, z, g]
    rain.append(s)

def draw_rain(s):
    x = s[0]
    y = s[1]
    r = s[2]
    z = s[3]

    pygame.draw.ellipse(screen, BLUE, [x, y, r, z])


def draw_sun():
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

def draw_grass():
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

def draw_tree():
    pygame.draw.rect(screen, BROWN, [160, 430, 20, 50])
    pygame.draw.polygon(screen, DARK_GREEN, [[100,430], [170,390], [240,430]])
    pygame.draw.polygon(screen, DARK_GREEN, [[110,410], [170,370], [230,410]])
    pygame.draw.polygon(screen, DARK_GREEN, [[120,390], [170,350], [220,390]])
    pygame.draw.polygon(screen, DARK_GREEN, [[130,370], [170,330], [210,370]])
    pygame.draw.polygon(screen, DARK_GREEN, [[140,350], [170,320], [200, 350]])

def draw_door():
    pygame.draw.rect(screen, PURPLE, [608, 395, 30, 55])
    pygame.draw.ellipse(screen, YELLOW, [630, 425, 5, 5])

def draw_window():
    pygame.draw.rect(screen, window, [565, 400, 25, 25])

def draw_roof():
    pygame.draw.polygon(screen, ORANGE, [[500, 350], [600, 300], [700, 350]])

def draw_house():
    pygame.draw.rect(screen, RED, [550, 350, 100, 100])



# Make clouds
num_clouds = 45
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])


daytime = True
lights_on = True
windy = True




# Block
loc = [380, 280]
vel = [0, 0]
speed = 5

def draw_block(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.rect(screen, WHITE, [x, y, 20, 20])
   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                daytime = not daytime
            elif event.key == pygame.K_x:
                lights_on = not lights_on
            elif event.key == pygame.K_RIGHT:
                vel[0] = speed
            elif event.key == pygame.K_LEFT:
                vel[0] = -1 * speed
            elif event.key == pygame.K_UP:
                vel[1] = -1 * speed
            elif event.key == pygame.K_DOWN:
                vel[1] = speed
            elif event.key == pygame.K_c:
                windy = not windy
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            elif event.key == pygame.K_LEFT:
                vel[0] = 0
            elif event.key == pygame.K_UP:
                vel[1] = 0
            elif event.key == pygame.K_DOWN:
                vel[1] = 0
            # google 'pygame key constants' for more keys

    # Game logic


    loc[0] += vel[0]
    loc[1] += vel[1]


    '''for p in plane:
        p[0] += 2'''

    
    for c in clouds:
        if windy:
            c[0] += 3
        else:
            c[0] += 1
        
        if c[0] > 900:
           c[0] = random.randrange(-800, 0)
           c[1] = random.randrange(-50, 200)

    for s in rain:
        if windy:
            s[0] += 2
            s[1] += 3

        else:
            s[0] += .5
            s[1] += 1.5

        if s[1] > s[4]:
            s[0] = random.randrange(-200, 800)
            s[1] = random.randrange(-50, 0)

#s[0] += .5
#s[1] += 1.5
#600


    ''' set sky color '''
    if daytime:
        sky = BLUE_GREY
    else:
        sky = BLACK
             
    # Drawing code
    ''' sky '''
    screen.fill(sky)



    ''' sun '''
    draw_sun()



    ''' grass '''
    draw_grass()

    '''plane'''
    '''for p in plane:
        draw_plane(p)'''
    
    '''rain'''    
    for s in rain:
        draw_rain(s)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],[x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    '''house'''
    draw_house()

    '''roof'''
    draw_roof()



    '''set light condition'''
    if lights_on:
        window = BRIGHT_YELLOW
    else:
        window = BLACK

    '''window'''
    draw_window()


    '''door'''
    draw_door()




    '''tree'''
    draw_tree()


    

    draw_block(loc)




    


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
