"""
Mini Project 3 Interactive Art
Katie & Shreya
Note: This code was based off code written in the Girls Who Code Summer immersion
program, which both Katie and Shreya particpated in. Katie wrote a very basic,
and slightly buggy version of this program in 2016 by combining the two activities
bouncing ball:
https://github.com/katie608/GWC/blob/master/python/Bounce_Ball_Green.py
and snow:
https://github.com/katie608/GWC/blob/master/python/Rainbow%20snow%20Bubbles.py
Since then, we have added a lot of new features.
"""

import pygame
import random
import math
import numpy as np

class Shape():
    '''
    Defines a generic shape class, with general characteristics of any shape.
    Attributes:
        x_location, y_location - coordinates of the center of the shape
        x_speed - number representing the speed of movement in the x direction
        y_speed - number representing speed of movement in the y direction
        size - number representing the size (range?)
        color_list - list of all possible colors that this shape could take
        color - tuple representing the color the shape, picked random from the color_list
        x_r - the coordinate of the shape if it were to be reflected across the y-axis
        y_d - the coordinates of the shape if it were to be reflected across the x-axis
    Functions:
        draw - renders the shape
        fall - makes the shape fall
        scroll - makes the shape scroll
        scatter - makes all shapes on the screen spread out chaotically
        bounce - like scatter, but the shapes reorient themselves randomly if they hit
        the edges of the screen
    '''
    def __init__(self, x_location, y_location, color_list, size):

        # Initializes the position of the shape
        self.x_location=x_location
        self.y_location=y_location

        # Initializes the speed of shape's movement
        self.x_speed = random.choice(possible_speeds)
        self.y_speed = random.choice(possible_speeds)

        # Initializes the appearance of the shape - size & color
        self.size = random.randint(5*size, 10*size) #7,15
        self.color_list = color_list
        self.color = color_list[random.randint(0, len(color_list) - 1)]

        # Calculates the position of the shape if it were reflected
        # Calculates the x-position, if the shape was reflected across the y-axis
        self.x_r =  SCREEN_WIDTH/2 + (SCREEN_WIDTH/2 - self.x_location)
        # Calculates the y-position, if the shape was reflected across the x-axis
        self.y_d = SCREEN_HEIGHT/2 + (SCREEN_HEIGHT/2 - self.y_location)

    def draw(self, screen):
        '''
        Draws the shape.
        This function is overwritten in all the subclasses of the Shape class,
        because each specific shape requires a different function from pygame
        to render it.
        '''
        pass

    def fall(self, screen):
        '''
        Causes the shape to fall down the screen, by incrementing the y-location of the shape.
        The amount incremented is the y_speed, which is a random number.
        '''
        self.draw(screen)

        #Adds the variable of speed to the variable of location every tick to make the circle move
        self.y_location += abs(self.y_speed)

    def scroll(self, screen):
        '''
        Causes the shape to scroll across the screen, by incrementing the x-location of the shape.
        The amount incremented is the x-axis, which is a random number.
        '''
        self.draw(screen)
        self.x_location += abs(self.x_speed)

    def scatter(self, screen):
        '''
        Causes the shape to scatter across the screen, by incrementing both the x-location
        and the y-location of the shape. The amounts incremented are the x_speed and
        y_speed respectively, which are both random numbers. This causes the shape
        to move in essentially a random direction.
        '''
        self.draw(screen)

        self.y_location += self.y_speed
        self.x_location += self.x_speed

    def bounce(self, screen):
        '''
        Causes the shape to scatter, but bounce and rebound in a random direction
        when it hits the edges of the screen.
        '''
        self.draw(screen)

        # Checks if the shape is at the edges of the screen
        # If the shape is at the left or right edges, then it reverses its x-direction of movement
        if self.x_location >= SCREEN_WIDTH - self.size or self.x_location < self.size:
            self.x_speed = self.x_speed * -1
        # If the shape is at the top or bottom, then it reverses its y-direction of movement
        if self.y_location >= SCREEN_HEIGHT - self.size or self.y_location < self.size:
            self.y_speed = self.y_speed * -1

        self.scatter(screen)

class Circle(Shape):
    '''
    Defines a Circle, which is a subclass of the Shape class.
    Has all the attributes and functionality of the Shape class.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Shape.__init__(self, x_location, y_location, color_list, size)

    def draw(self, screen):
        '''
        Draws a circle on the screen using pygame's draw function.
        '''
        pygame.draw.circle(screen, self.color, [int(self.x_location), int(self.y_location)], self.size)

    def mirror_y(self):
        '''
        Mirrors the circle across the y-axis.
        '''
        # Creates a mirrored Circle with the same size as the origional one
        mirrored = Circle(self.x_r, self.y_location, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_x(self):
        '''
        Mirrors the circle across the x-axis.
        '''
        # Creates a mirrored Circle
        mirrored = Circle(self.x_location, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_both(self):
        '''
        Mirrors the circle across both the x-axis and the y-axis.
        '''
        # Creates a mirrored Circle
        mirrored = Circle(self.x_r, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

class Polygon(Shape):
    '''
    Defines a Polygon object, which is a subclass of the Shape class.
    Has all the attributes of the Shape class, along with:
        points_list - the list of points defining the vertices of the polygon,
        with each point as a list with two elements
    Has all the functions of the Shape class.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Shape.__init__(self, x_location, y_location, color_list, size)
        self.get_points_list()

    def get_points_list(self):
        '''
        Creates the list of points defining the vertices of the polygon.
        Will be overwritten by every subclass of Polygon.
        '''
        self.points_list = [[int(self.x_location), int(self.y_location)]]

    def draw(self, screen):
        '''
        Draws the polygon on the screen.
        '''
        # Updates the points list
        self.get_points_list()
        pygame.draw.polygon(screen, self.color, self.points_list, self.size)


class Triangle(Polygon):
    '''
    Defines a Triangle object, which is a subclass of the Polygon class.
    Has all the attributes and functions of the Polygon class.
    The Triangle's points list contains three points, with each point
    representing on vertex of the triangle.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Polygon.__init__(self, x_location, y_location, color_list, size)

    def get_points_list(self):
        self.top_vertex = [self.x_location, self.y_location - (2/3)*self.size]
        self.left_vertex = [self.x_location - (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.right_vertex = [self.x_location + (1/2)*self.size, self.y_location + (1/3)*self.size]
        self.points_list = [self.top_vertex, self.left_vertex, self.right_vertex]

    def draw(self, screen, line_thickness = 2):
        self.get_points_list()
        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

    def mirror_y(self):
        mirrored = Triangle(self.x_r, self.y_location, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_x(self):
        mirrored = Triangle(self.x_location, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_both(self):
        mirrored = Triangle(self.x_r, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

class Bow_tie(Polygon):
    '''
    Defines the Bowtie object, which is a subclass of the Polygon class.
    Has all the attributes and functions of the Polygon class.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Polygon.__init__(self, x_location, y_location, color_list, size)

    def get_points_list(self):
        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def draw(self, screen, line_thickness = 2):
        self.get_points_list()
        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

    def mirror_y(self):
        mirrored = Bow_tie(self.x_r, self.y_location, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_x(self):
        mirrored = Bow_tie(self.x_location, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_both(self):
        mirrored = Bow_tie(self.x_r, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

class Square(Polygon):
    '''
    Defines a Square object, which is a subclass of the Polygon class.
    Has all the attributes and functions of the Polygon object.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Polygon.__init__(self, x_location, y_location, color_list, size)

    def get_points_list(self):
        self.vertex1 = [self.x_location+(1/2)*self.size, self.y_location+(1/2)*self.size]
        self.vertex2 = [self.x_location+(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex3 = [self.x_location-(1/2)*self.size, self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location-(1/2)*self.size, self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def draw(self, screen, line_thickness = 2):
        self.get_points_list()
        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

    def mirror_y(self):
        mirrored = Square(self.x_r, self.y_location, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_x(self):
        mirrored = Square(self.x_location, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_both(self):
        mirrored = Square(self.x_r, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

class Hexagon(Polygon):
    '''
    Defines a Hexagon object, which is a subclass of the Polygon class.
    Has all the attributes and function of a Polygon.
    '''
    def __init__(self, x_location, y_location, color_list, size):
        Polygon.__init__(self, x_location, y_location, color_list, size)

    def get_points_list(self):
        self.vertex1 = [self.x_location, self.y_location+self.size]
        self.vertex2 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]
        self.vertex3 = [self.x_location+self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex4 = [self.x_location, self.y_location-self.size]
        self.vertex5 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location-(1/2)*self.size]
        self.vertex6 = [self.x_location-self.size*math.sin(math.pi/3), self.y_location+(1/2)*self.size]

        self.points_list = [self.vertex1, self.vertex2, self.vertex3,
                            self.vertex4, self.vertex5, self.vertex6]

    def draw(self, screen, line_thickness = 2):
        self.get_points_list()
        pygame.draw.polygon(screen, self.color, self.points_list, line_thickness)

    def mirror_y(self):
        mirrored = Hexagon(self.x_r, self.y_location, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_x(self):
        mirrored = Hexagon(self.x_location, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

    def mirror_both(self):
        mirrored = Hexagon(self.x_r, self.y_d, self.color_list, self.size)
        mirrored.size = self.size
        return mirrored

def print_instructions():
    '''
    Prints the instructions for the user to the terminal.
    '''
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
    print("6: mirror across the y-axis")
    print("7: mirror across the x-axis")
    print("8: mirror diagonally (over the origin)")
    print("9: mirror in all directions")
    print("SPACE: goes to the next mode (and loops back)")
    print("+: increases size")
    print("-: decreases size")
    print("up and down keys cycle through different shapes")
    print("CTRL+Z: undos")

if __name__ == "__main__":
    # Defines some colors
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

    # Defines color lists:
    all_colors = [RED, REDORANGE, ORANGE, YELLOWORANGE, YELLOW, YELLOWGREEN, GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO, LIGHTPURPLE, PURPLE, DARKPURPLE, MAGENTA, PINK, BLACK, DARKGREY, GREY, LIGHTGREY, WHITE, BROWN, DARKBROWN]
    ocean_colors = [DARKGREEN,BLUEGREEN,CYAN,SKYBLUE,BLUE,INDIGO,NIGHTSKY,DARKPURPLE,DARKGREY]
    pastel_colors = [LIGHTGREY,LIGHTPURPLE,PINK,WHITE,SKYBLUE]
    warm_colors = [RED,REDORANGE,ORANGE,YELLOWORANGE,YELLOW,MAGENTA,PINK]
    reds_greens = [RED,REDORANGE,YELLOWGREEN,GREEN,DARKGREEN,BLUEGREEN]

    # Defines the various modes
    DRAW_MODE = 1
    FALL_MODE = 2
    SCROLL_MODE = 3
    SCATTER_MODE = 4
    BOUNCE_MODE = 5
    MIRROR_Y_MODE = 6
    MIRROR_X_MODE = 7
    MIRROR_DIAGONAL_MODE = 8
    MIRROR_ALL_MODE = 9

    # Creates list of possible x and y speeds for objects
    possible_speeds = [-3, -2, -1, 1, 2, 3]

    # Tells the pygame program for python to start
    pygame.init()

    # Set the width and height of the screen [width, height] and defines the screen
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Sets the caption at the top
    pygame.display.set_caption("Drawing Game")

    # Controls when the game quits
    done = False

    # Controls how fast the screen updates
    clock = pygame.time.Clock()

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
        for event in pygame.event.get():

            # Checks to see if the user has clicked on the close out button on
            # the pygame console
            if event.type == pygame.QUIT:
                done = True

            # Checks whether the user is drawing
            elif event.type==pygame.MOUSEBUTTONDOWN:
                drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False

            # Changes relevant characteristics of the drawing, if the associated
            # keys are pressed
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                mods = pygame.key.get_mods()
                # Clears screen if the C key is pressed
                if keys[pygame.K_c]:
                    shape_list.clear()

            # Changes the color list
            # Selects all colors if the A key is pressed
                elif keys[pygame.K_a]:
                    color_list = all_colors
                elif keys[pygame.K_s]:
                        # Saves screenshot of the screen if CTRL+S is pressed
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
                    mode = DRAW_MODE
                elif keys[pygame.K_2]:
                    mode = FALL_MODE
                elif keys[pygame.K_3]:
                    mode = SCROLL_MODE
                elif keys[pygame.K_4]:
                    mode = SCATTER_MODE
                elif keys[pygame.K_5]:
                    mode = BOUNCE_MODE
                elif keys[pygame.K_6]:
                    mode = MIRROR_Y_MODE
                elif keys[pygame.K_7]:
                    mode = MIRROR_X_MODE
                elif keys[pygame.K_8]:
                    mode = MIRROR_DIAGONAL_MODE
                elif keys[pygame.K_9]:
                    mode = MIRROR_ALL_MODE
                elif keys[pygame.K_SPACE]:
                    mode += 1
                    if mode == MIRROR_ALL_MODE:
                        mode = 0

# keys for manipulating size
                elif keys[pygame.K_MINUS]:
                    if size <= 1:
                        size = 1
                    else:
                        size -= 1
                elif keys[pygame.K_EQUALS] or keys[pygame.K_PLUS]:
                    size += 1
# Changes the shape type
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

# Removes the five most recently drawn shapes when CTRL+Z is pressed
                elif keys[pygame.K_z] and mods & pygame.KMOD_CTRL:
                    shape_list = shape_list[:len(shape_list)-5]


# quits when q is pressed
                elif keys[pygame.K_q]:
                    done = True

# Draws on the screen
        if drawing:
            # gets mouse position
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            # calculates inverse x and y coordinates for mirroring function
            x_r = SCREEN_WIDTH/2 + (SCREEN_WIDTH/2 - x)
            y_d = SCREEN_HEIGHT/2 + (SCREEN_HEIGHT/2 - y)
            # creates list of types of shapes that can be added to list
            shape_types = [Circle(x, y, color_list, size),
            Square(x, y, color_list, size),
            Triangle(x, y, color_list, size),
            Hexagon(x, y, color_list, size),
            Bow_tie(x, y, color_list, size)]
            # determines how many shapes to add to list, and does so
            curr_shape = shape_types[shape_type]
            if mode == MIRROR_Y_MODE:
                shape_list.append(curr_shape)
                shape_list.append(curr_shape.mirror_y())
            elif mode == MIRROR_X_MODE:
                shape_list.append(curr_shape)
                shape_list.append(curr_shape.mirror_x())
            elif mode == MIRROR_DIAGONAL_MODE:
                shape_list.append(curr_shape)
                shape_list.append(curr_shape.mirror_both())
            elif mode == MIRROR_ALL_MODE:
                shape_list.append(curr_shape)
                shape_list.append(curr_shape.mirror_x())
                shape_list.append(curr_shape.mirror_y())
                shape_list.append(curr_shape.mirror_both())
            else:
                shape_list.append(curr_shape)

        # Sets background color
        screen.fill(BLACK)

        # Animates or draws all shapes
        for shape in shape_list:
            if mode == DRAW_MODE or mode == MIRROR_Y_MODE or mode == MIRROR_X_MODE or mode == MIRROR_DIAGONAL_MODE or mode == MIRROR_ALL_MODE:
                shape.draw(screen)
            elif mode == FALL_MODE:
                shape.fall(screen)
            elif mode == SCROLL_MODE:
                shape.scroll(screen)
            elif mode == SCATTER_MODE:
                shape.scatter(screen)
            elif mode == BOUNCE_MODE:
                shape.bounce(screen)

        # updates screen
        pygame.display.flip()
        # controls how fast game updates
        clock.tick(60)

    # quits pygame and exits window if done
    pygame.quit()
    exit()
