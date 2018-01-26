# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
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
SHADOW = (0, 20, 0)


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



   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 1
        
        if c[0] > 900:
           c[0] = random.randrange(-800, 0)
           c[1] = random.randrange(-50, 200)



    for s in rain:
        s[0] += .5
        s[1] += 1.5

        if s[1] > s[4]:
            s[0] = random.randrange(-200, 800)
            s[1] = random.randrange(-50, 0)

#s[0] += .5
#s[1] += 1.5
#600


    
    # Drawing code
    '''Background sky '''
    screen.fill(NIGHT)
        
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    '''tree'''
    pygame.draw.rect(screen, BROWN, [160, 430, 20, 50])
    pygame.draw.polygon(screen, DARK_GREEN, [[100,430], [170,390], [240,430]])
    pygame.draw.polygon(screen, DARK_GREEN, [[110,410], [170,370], [230,410]])
    pygame.draw.polygon(screen, DARK_GREEN, [[120,390], [170,350], [220,390]])
    pygame.draw.polygon(screen, DARK_GREEN, [[130,370], [170,330], [210,370]])
    pygame.draw.polygon(screen, DARK_GREEN, [[140,350], [170,320], [200, 350]])



    '''rain'''    
    for s in rain:
        draw_rain(s)


    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
