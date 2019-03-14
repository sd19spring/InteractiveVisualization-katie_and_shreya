"""Mini Project 3 Interactive Art
Katie & Shreya
"""

import pygame
import random


# Define some colors
RED=(255, 0, 0)
REDORANGE=(230, 50, 0)
ORANGE=(230, 120, 0)
YELLOWORANGE=(250, 160, 0)
YELLOW=(250, 210, 0)
YELLOWGREEN=(230, 230, 0)
GREEN=(0,255 , 0)
DARKGREEN=(0, 100, 0)
BLUEGREEN=(0, 150, 100)
CYAN=(0, 255, 225)
SKYBLUE=(100, 150, 255)
BLUE=(0, 0, 255)
INDIGO=(30, 0, 100)
NIGHTSKY=(0, 0, 30)
LIGHTPURPLE=(160, 100, 255)
PURPLE=(130, 0, 220)
DARKPURPLE=(40, 0, 100)
MAGENTA=(200, 0, 200)
PINK=(250, 120, 250)
HEART=(230, 65, 60)
BLACK=(0, 0, 0)
DARKGREY=(60, 60, 60)
GREY=(120, 120, 120)
LIGHTGREY=(180, 180, 180)
WHITE=(255, 255, 255)
TAN=(105, 65, 45)
BROWN=(120, 70, 15)
DARKBROWN=(80, 40, 10)

#Tells the pygame program for python to start
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Sets the caption at the top
pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# All color lists:
all_colors = [RED, REDORANGE, ORANGE, YELLOWORANGE, YELLOW, YELLOWGREEN, GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO, LIGHTPURPLE, PURPLE, DARKPURPLE, MAGENTA, PINK, BLACK, DARKGREY, GREY, LIGHTGREY, WHITE, BROWN, DARKBROWN]
ocean_colors = [DARKGREEN,BLUEGREEN,CYAN,SKYBLUE,BLUE,INDIGO,NIGHTSKY,DARKPURPLE,DARKGREY]
pastel_colors = [LIGHTGREY,LIGHTPURPLE,PINK,WHITE,SKYBLUE]
warm_colors = [RED,REDORANGE,ORANGE,YELLOWORANGE,YELLOW,MAGENTA,PINK]
reds_greens = [RED,REDORANGE,YELLOWGREEN,GREEN,DARKGREEN,BLUEGREEN]

possible_speeds = [-3, -2, -1, 1, 2, 3]


#Defines the class of circle(some charactaristics of the circle and everything it does)
class Circle():
    def __init__(self, x_location, y_location, color_list, size):
        self.x_location=x_location
        self.y_location=y_location
        #you can change the speeds here by making them equal to something else
        self.x_speed = random.choice(possible_speeds)
        self.y_speed = random.choice(possible_speeds)
        #you can change the size here
        self.size = random.randint(5*size, 10*size) #7,15
        # self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        self.color = color_list[random.randint(0,len(color_list)-1)]

    #Defines the function move that draws the circles and makes them move offscreen
    def Move(self, screen):
        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.size)

        #Adds the variable of speed to the variable of location every tick to make the circle move
        self.y_location += self.y_speed
        self.x_location += self.x_speed

    #Defines the bounce function that draws the circles and makes them bounce when they reach the sides
    def Fall(self, screen):
        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.size)

        #Adds the variable of speed to the variable of location every tick to make the circle move
        self.y_location += 1#abs(self.y_speed)

    def Scroll(self, screen):
        self.x_location += 1 #abs(self.x_speed)

    def Bounce(self, screen):
        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.size)

        #Tells ball to turn around when it reaches the edge of the screen
        if self.x_location >= SCREEN_WIDTH - self.size or self.x_location < self.size:
            self.x_speed = self.x_speed * -1
        if self.y_location >= SCREEN_HEIGHT - self.size or self.y_location < self.size:
            self.y_speed = self.y_speed * -1

        #Makes circles move
        self.x_location += self.x_speed
        self.y_location += self.y_speed

    def Stay(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.x_location), int(self.y_location)], self.size)



print("Use Number keys to change size, use asdf to change color, use c to clear and q to quit")

#Creates ball list that the circles can be added to later
shape_list = []

drawing = False
color_list = all_colors
size = 2
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                shape_list.clear()
            elif event.key == pygame.K_a:
                color_list = all_colors
            elif event.key == pygame.K_s:
                color_list = ocean_colors
            elif event.key == pygame.K_d:
                color_list = pastel_colors
            elif event.key == pygame.K_f:
                color_list = warm_colors
            elif event.key == pygame.K_g:
                color_list = reds_greens

            elif event.key == pygame.K_1:
                size = 1
            elif event.key == pygame.K_2:
                size = 2
            elif event.key == pygame.K_3:
                size = 3
            elif event.key == pygame.K_4:
                size = 4
            elif event.key == pygame.K_5:
                size = 5
            elif event.key == pygame.K_6:
                size = 6
            elif event.key == pygame.K_7:
                size = 7
            elif event.key == pygame.K_8:
                size = 8
            elif event.key == pygame.K_9:
                size = 9

            elif event.key == pygame.K_q:
                done = True


    if drawing:
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        shape_list.append(Circle(x, y, color_list, size))



    #Background color
    screen.fill(BLACK)

    #tells all balls in the list to fall
    for Shape in shape_list:
        # Ball.Stay(screen)
        Shape.Fall(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()
