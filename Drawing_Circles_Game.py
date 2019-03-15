"""Mini Project 3 Interactive Art
Katie & Shreya
"""

import pygame
import random
import math


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
class Shape():
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

    def draw(self, screen):
        pass

    #Defines the bounce function that draws the circles and makes them bounce when they reach the sides
    def fall(self, screen):
        self.draw(screen)

        #Adds the variable of speed to the variable of location every tick to make the circle move
        self.y_location += 1#abs(self.y_speed)

    def scroll(self, screen):
        self.draw(screen)
        self.x_location += 1 #abs(self.x_speed)
    #Defines the function move that draws the circles and makes them move offscreen

    def scatter(self, screen):
        self.draw(screen)

        #Adds the variable of speed to the variable of location every tick to make the circle move
        self.y_location += self.y_speed
        self.x_location += self.x_speed

    def bounce(self, screen):
        self.draw(screen)

        #Tells ball to turn around when it reaches the edge of the screen
        if self.x_location >= SCREEN_WIDTH - self.size or self.x_location < self.size:
            self.x_speed = self.x_speed * -1
        if self.y_location >= SCREEN_HEIGHT - self.size or self.y_location < self.size:
            self.y_speed = self.y_speed * -1

        #Makes circles move
        self.x_location += self.x_speed
        self.y_location += self.y_speed

class Circle(Shape):
    def __init__(self, x_location, y_location, color_list, size):
        Shape.__init__(self, x_location, y_location, color_list, size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.x_location), int(self.y_location)], self.size)

class Polygon(Shape):
    def __init__(self, x_location, y_location, color_list, size, sides):
        Shape.__init__(self, x_location, y_location, color_list, size)
        self.sides = sides

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [int(self.x_location), int(self.y_location)], self.size)

class Triangle(Polygon):
    def __init__(self, x_location, y_location, color_list, size, sides=3):
        Polygon.__init__(self, x_location, y_location, color_list, size, sides)
        self.median = math.sqrt(self.size**2 + (self.size/2)**2)

    def draw(self, screen, line_thickness = 2):

        top_vertex = [self.x_location, self.y_location + (2/3)*self.size]
        left_vertex = [self.x_location - (1/2)*self.size, self.y_location - (1/3)*self.size]
        right_vertex = [self.x_location + (1/2)*self.size, self.y_location - (1/3)*self.size]

        pygame.draw.polygon(screen, self.color, [right_vertex, top_vertex, left_vertex], line_thickness)

print("Use Number keys to change size, use asdf to change color, use c to clear and q to quit")

#Creates ball list that the circles can be added to later
shape_list = []

drawing = False
color_list = all_colors
mode = 1
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
            keys = pygame.key.get_pressed()
            mods = pygame.key.get_mods()

            if keys[pygame.K_c]:
                shape_list.clear()
            elif keys[pygame.K_a]:
                color_list = all_colors
            elif keys[pygame.K_s]:
                if mods & pygame.KMOD_CTRL:
                    pygame.image.save(screen, "screenshot.jpg")
                else:
                    color_list = ocean_colors
            elif keys[pygame.K_d]:
                color_list = pastel_colors
            elif keys[pygame.K_f]:
                color_list = warm_colors
            elif keys[pygame.K_g]:
                color_list = reds_greens

            elif keys[pygame.K_1]:
                mode = 1
            elif keys[pygame.K_2]:
                mode = 2
            elif keys[pygame.K_3]:
                mode = 3
            elif keys[pygame.K_4]:
                mode = 4
            elif keys[pygame.K_5]:
                mode = 5

            elif event.key == pygame.K_MINUS:
                if size <= 1:
                    size = 1
                else:
                    size -= 1
            elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                size += 1


            elif event.key == pygame.K_SPACE:
                mode += 1
                if mode == 6:
                    mode = 0

            elif event.key == pygame.K_q:
                done = True


    if drawing:
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        shape_list.append(Triangle(x, y, color_list, size))



    #Background color
    screen.fill(BLACK)

    #tells all balls in the list to fall
    for shape in shape_list:
        # Ball.Stay(screen)
        if mode == 1:
            shape.draw(screen)
        elif mode == 2:
            shape.fall(screen)
        elif mode == 3:
            shape.scroll(screen)
        elif mode == 4:
            shape.scatter(screen)
        elif mode == 5:
            shape.bounce(screen)




    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()
