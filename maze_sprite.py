import pygame
from pygame.locals import *

class maze:
    """
    Setup the maze into four parts.
    """
    def __init__(self):
        self.tile_size = 20

class button:
    """
    button class in the game.

    Parameters:
        x & y (int) - coordinates on the screen where to place them
        width & height (int) - the size of the button
        name (str) - the button name displayed
        color (tuple of int) - color of the button you want in rgb format (rrr,ggg,bbb)
    """
    def __init__(self, x:int, y:int, width:int, height:int, color, name:str =''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.color = color
        self.name = name
    
    def draw(self, win, outline, fsize):
        pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4)) 
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.name != '':
            font = pygame.font.SysFont('mvboli', fsize)
            name = font.render(self.name, 1, (0, 0, 0))
            win.blit(name, (self.x + (self.width/2 - name.get_width()/2), self.y + (self.height/2 - name.get_height()/2)))

    def is_over(self, pos):
        # pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class setup:
    """
    Starts the game according to specified setup.
    """
    def __init__(self):
        pygame.init()
        
        # Game screen size
        self.screen_width = 1760
        self.screen_height = 990

        # Number of FPS
        self.clock = pygame.time.Clock()

        # Set screen size
        self.screen = pygame.display.set_mode((self.screen_width,self.
                                               screen_height))
        pygame.display.set_caption('Maze Runner')

        # Variables that stops the game when set to false
        self.running = True
        self.dt = 0

        # Game background
        self.hell_bg = pygame.image.load('img\hell.jpg')
        self.hell_bg_resized = pygame.transform.scale(self.hell_bg, (self.screen_width, self.screen_height))

        # Button parameters
        self.b_height = 120
        self.b_width = 220
        self.b_x = (self.screen_width - self.b_width) // 2
        self.b_color = (79, 6, 6)

        # Buttons and placement in screen
        self.start = button(x=self.b_x, y=200, width=self.b_width, height=self.b_height, color=self.b_color, name="Escape")
        self.instruction = button(x=self.b_x, y=350, width=self.b_width, height=self.b_height, color=self.b_color, name="Instruction")

        # Maze map
        self.maze = maze

    def run(self):
        while self.running:
            # Show the background and design (Take note that the order matters to show all images)
            self.screen.blit(self.hell_bg_resized, (0,0))

            # Show elements such as buttons, images, text
            self.start.draw(self.screen, (18, 1, 1), 60) # start button
            self.instruction.draw(self.screen, (18, 1, 1),42) # instruction button

            # Handle all events
            self.event_handler()

            # Limit fps to 60
            self.clock.tick(60)

            # Update the frame at each iteration
            pygame.display.update()

        pygame.quit()

    def event_handler(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            # if the game is closed
            if event.type == pygame.QUIT:
                self.running = False

            # If the mouse is click check through all possible buttons that are clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start.is_over(pos):
                    print('this is difficulty page')
                if self.instruction.is_over(pos):
                    print('this is instruction page')

            if event.type == pygame.MOUSEMOTION:
                if self.start.is_over(pos):
                    self.start.color = (38, 3, 3)
                else:
                    self.start.color = self.b_color

                if self.instruction.is_over(pos):
                    self.instruction.color = (38, 3, 3)
                else:
                    self.instruction.color = self.b_color

