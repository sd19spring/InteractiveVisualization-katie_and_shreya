"""
Mini Project 3 Interactive Art
Katie & Shreya
This is the version that Katie used to mess around with simplifying the
mirroring code. It also has a working control-z
"""

import pygame
import random
import math
import numpy as np


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
SCREEN_HEIGHT = 800

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
        self.color_list = color_list
        self.color = color_list[random.randint(0, len(color_list) - 1)]

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

    def rotate(self, screen):
        pass

    def mirror(self, screen):
        self.draw(screen)
        mirrored = Shape(self.x_location + 50, self.y_location, self.color_list, self.size)
        mirrored.draw(screen)

class Circle(Shape):
    def __init__(self, x_location, y_location, color_list, size):
        Shape.__init__(self, x_location, y_location, color_list, size)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.x_location), int(self.y_location)], self.size)

    # def mirror(self, screen):
    #     self.draw(screen)
    #     mirrored = Circle(self.x_location + 50, self.y_location, self.color_list, self.size)
    #     mirrored.draw(screen)

class Polygon(Shape):
    def __init__(self, x_location, y_location, color_list, size, sides):
        Shape.__init__(self, x_location, y_location, color_list, size)
        self.sides = sides
        self.points_list = [[int(self.x_location), int(self.y_location)]]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points_list, self.size)

    # def rotate(self, screen, theta):
    #     theta = theta*math.pi/180
    #     rot_1 = [math.cos(theta), math.sin(theta)]
    #     rot_2 = [-math.sin(theta), math.cos(theta)]
    #
    #     rotation_matrix = np.array([rot_1, rot_2])
    #     points_x = []
    #     points_y = []
    #     for point in self.points_list:
    #         points_x.append(point[0])
    #         points_y.append(point[1])
    #
    #     points = np.array([points_x, points_y])
    #     rotated_points = np.matmul(rotation_matrix, points)
    #
    #     rot_points_x = rotated_points[0]
    #     rot_points_y = rotated_points[1]
    #
    #     rot_points = []
    #     for i in range(len(rot_points_x)):
    #         point = [rot_points_x[i], rot_points_y[i]]
    #         rot_points.append(point)
    #     print(rot_points)
    #
    #     self.points_list = rot_points
    #     return self


class Triangle(Polygon):
    def __init__(self, x_location, y_location, color_list, size, sides=3):
        Polygon.__init__(self, x_location, y_location, color_list, size, sides)
        self.median = math.sqrt(self.size**2 + (self.size/2)**2)

        self.top_vertex = [self.x_location, self.y_location - (2/3)*self.size]
        self.left_vertex = [self.x_location - (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.right_vertex = [self.x_location + (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.points_list = [self.top_vertex, self.left_vertex, self.right_vertex]

    def draw(self, screen, line_thickness = 2):

        self.top_vertex = [self.x_location, self.y_location - (2/3)*self.size]
        self.left_vertex = [self.x_location - (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.right_vertex = [self.x_location + (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.points_list = [self.top_vertex, self.left_vertex, self.right_vertex]

        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

class Bow_tie(Polygon):
    def __init__(self, x_location, y_location, color_list, size, sides=4):
        Polygon.__init__(self, x_location, y_location, color_list, size, sides)
        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def draw(self, screen, line_thickness = 2):

        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

class Square(Polygon):
    def __init__(self, x_location, y_location, color_list, size, sides=4):
        Polygon.__init__(self, x_location, y_location, color_list, size, sides)
        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def draw(self, screen, line_thickness = 2):

        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

class Hexagon(Polygon):
    def __init__(self, x_location, y_location, color_list, size, sides=6):
        Polygon.__init__(self, x_location, y_location, color_list, size, sides)
        self.vertex1 = [self.x_location, self.y_location+self.size]
        self.vertex2 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]
        self.vertex3 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location, self.y_location-self.size]
        self.vertex5 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex6 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3,
                            self.vertex4, self.vertex5, self.vertex6]

    def draw(self, screen, line_thickness = 2):

        self.vertex1 = [self.x_location, self.y_location+self.size]
        self.vertex2 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]
        self.vertex3 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location, self.y_location-self.size]
        self.vertex5 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex6 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3,
                            self.vertex4, self.vertex5, self.vertex6]

        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

def print_instructions():
    print("\nWelcome to our drawing game! Here's some tips to get you started.\n")

    print("GENERAL KEY COMMANDS:")
    print("CTRL + S: saves image")
    print("c: clears the screen")
    print("Q: quits\n")
    print("APPEARANCE OPTIONS:")
    print("a: all colors")
    print("s: ocean color palette")
    print("d: pastel color palette")
    print("f: warm color palette")
    print("g: reds and greens\n")
    print("Shapes are in this order: Circle, Triangle, Hexagon, Square, Bowtie")
    print("UP: go to the next shape")
    print("DOWN: go to the previous shape")
    print("MOVEMENT/SIZE OPTIONS:")
    print("1: stay still")
    print("2: fall")
    print("3: scroll")
    print("4: scatter")
    print("5: bounce")
    print("SPACE: goes to the next mode (and loops back)")
    print("+: increases size")
    print("-: decreases size")
    print("up and down keys cycle through different shapes")

print_instructions()

#Creates ball list that the circles can be added to later
shape_list = []

drawing = False
color_list = all_colors
mode = 1
size = 2
shape_type = 0


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

# gets key that is pressed, determines which key that is, and acts accordingly
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            mods = pygame.key.get_mods()

            if keys[pygame.K_c]:
                shape_list.clear()

# keys for changing color scheme
            elif keys[pygame.K_a]:
                color_list = all_colors
            elif keys[pygame.K_s]:
                if mods & pygame.KMOD_CTRL:
                    filename = str(input("Enter a name for the screenshot: ")) + ".jpg"
                    pygame.image.save(screen, filename)
                else:
                    color_list = ocean_colors
            elif keys[pygame.K_d]:
                color_list = pastel_colors
            elif keys[pygame.K_f]:
                color_list = warm_colors
            elif keys[pygame.K_g]:
                color_list = reds_greens

# keys for manipulating modes (drawing, bouncing, scrolling, etc)
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
            elif keys[pygame.K_6]:
                mode = 6
            elif keys[pygame.K_7]:
                mode = 7
            elif keys[pygame.K_SPACE]:
                mode += 1
                if mode == 7:
                    mode = 0

# keys for manipulating size
            elif keys[pygame.K_MINUS]:
                if size <= 1:
                    size = 1
                else:
                    size -= 1
            elif keys[pygame.K_EQUALS] or keys[pygame.K_PLUS]:
                size += 1

            elif keys[pygame.K_UP]:
                if shape_type == 4:
                    shape_type = 0
                else:
                    shape_type += 1
            elif keys[pygame.K_DOWN]:
                if shape_type == 0:
                    shape_type = 4
                else:
                    shape_type -= 1

# Key for undoing
            elif keys[pygame.K_z] and mods & pygame.KMOD_CTRL:
                shape_list = shape_list[:len(shape_list)-5]


# quits when q is pressed
            elif keys[pygame.K_q]:
                done = True

    if drawing:
        pos=pygame.mouse.get_pos()
        x=pos[0]
        y=pos[1]
        x_r = SCREEN_WIDTH/2 + (SCREEN_WIDTH/2 - x)
        y_r = SCREEN_HEIGHT/2 + (SCREEN_HEIGHT/2 - y)

        shape_types = [Circle,Square,Triangle,Hexagon,Bow_tie]

        if mode == 6:
            shape_list.append(shape_types[shape_type](x,y,color_list,size))
            shape_list.append(shape_types[shape_type](x_r,y,color_list,size))
        elif mode == 7:
            shape_list.append(shape_types[shape_type](x,y,color_list,size))
            shape_list.append(shape_types[shape_type](x_r,y,color_list,size))
            shape_list.append(shape_types[shape_type](x,y_r,color_list,size))
            shape_list.append(shape_types[shape_type](x_r,y_r,color_list,size))
        else:
            shape_list.append(shape_types[shape_type](x,y,color_list,size))

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
        elif mode == 6 or mode == 7:
            shape.mirror(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit()
