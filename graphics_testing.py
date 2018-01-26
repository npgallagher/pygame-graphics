# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Cool Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
PURPLE = (128, 0 , 128)
TEAL = (0, 128, 128)
AQUA = (0, 255, 255)
BROWN = (139, 69, 19)
DARK_GREEN = (0, 100, 0)
MEDIUM_GREEN = (0, 150, 0)


def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])



def draw_flower(x, y):
    pygame.draw.rect(screen, MEDIUM_GREEN, [x+10, y + 15, 5, 10])
    pygame.draw.ellipse(screen, WHITE, [x+8,y+8,9,9])
    pygame.draw.ellipse(screen, YELLOW, [x+8,y+1, 9, 9])
    pygame.draw.ellipse(screen, WHITE, [x+8, y-6, 9, 9])
    pygame.draw.ellipse(screen, WHITE, [x-1, y+1, 9, 9])
    pygame.draw.ellipse(screen, WHITE, [x+17, y+1, 9, 9])

    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    '''sky'''
    screen.fill(AQUA)

    '''sun'''
    pygame.draw.circle(screen, YELLOW, [650, 100], 50)

    ''' clouds '''
    draw_cloud(50, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)


    
    '''grass'''
    pygame.draw.rect(screen, GREEN, [0, 450, 800, 150])


    '''fence1'''
    y = 408
    for x in range(5, 800, 30):
        post = [[x + 5, y], [x + 10, y + 5], [x+10, y + 40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, 418, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, 438, 800, 5])



    '''house'''
    pygame.draw.rect(screen, RED, [550, 350, 100, 100])

    '''roof'''
    pygame.draw.polygon(screen, ORANGE, [[500, 350], [600, 300], [700, 350]])


    '''window'''
    pygame.draw.rect(screen, YELLOW, [565, 400, 25, 25])


    '''door'''
    pygame.draw.rect(screen, PURPLE, [608, 395, 30, 55])
    pygame.draw.ellipse(screen, YELLOW, [630, 425, 5, 5])


    '''tree'''
    pygame.draw.rect(screen, BROWN, [160, 430, 20, 50])
    pygame.draw.polygon(screen, DARK_GREEN, [[100,430], [170,390], [240,430]])
    pygame.draw.polygon(screen, DARK_GREEN, [[110,410], [170,370], [230,410]])
    pygame.draw.polygon(screen, DARK_GREEN, [[120,390], [170,350], [220,390]])
    pygame.draw.polygon(screen, DARK_GREEN, [[130,370], [170,330], [210,370]])
    pygame.draw.polygon(screen, DARK_GREEN, [[140,350], [170,320], [200, 350]])



    '''flowers'''
    draw_flower(50, 500)
    draw_flower(500, 480)
    draw_flower(347, 460)


    
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
    #pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
