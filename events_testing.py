# Computer Programming 1
# Unit 11 - Graphics
#


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
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)


# Make clouds
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(-800, 800)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])


#Tree

def draw_tree():
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)

    pygame.draw.rect(screen, BROWN, [x, x+270, 20, 50])#160
    pygame.draw.polygon(screen, DARK_GREEN, [[x-60,x+270], [x+10,x+230], [x+80,x+270]])
    pygame.draw.polygon(screen, DARK_GREEN, [[x-50,x+250], [x+10,x+210], [x+70,x+250]])
    pygame.draw.polygon(screen, DARK_GREEN, [[x-40,x+230], [x+10,x+190], [x+60,x+230]])
    pygame.draw.polygon(screen, DARK_GREEN, [[x-30,x+210], [x+10,x+170], [x+50,x+210]])
    pygame.draw.polygon(screen, DARK_GREEN, [[x-20,x+190], [x+10,x+160], [x+40, x+190]])




daytime = True
lights_on = False
trees = False


   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
        elif event.type == pygame.K_c:
            trees = True
            # google 'pygame key constants' for more keys

    # Game logic
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-800, 0)
           c[1] = random.randrange(-50, 200)


    ''' set sky color '''
    if daytime:
        sky = BLUE
    else:
        sky = BLACK
             
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],[x+10, y+40], [x, y+40],[x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)



    if trees == True:
        draw_tree()

    


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
