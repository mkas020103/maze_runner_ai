import pygame
from pygame.locals import *
import map

class Block:
    """
    Block that build up the maze (i.e. path, portal, powerup, wall)
    """
    def __init__(self, block_image, tile, col, row, position):
        self.tile_size = tile
        # Transform the image size
        self.block = pygame.transform.scale(block_image, (self.tile_size, self.tile_size))
        # makes the image a "rectangle" object of pygame
        self.block_rect = self.block.get_rect()
        # Plot the x and y coordinates of the image
        self.block_rect.x = col * self.tile_size + position
        self.block_rect.y = row * self.tile_size + position

    def give(self):
        return (self.block, self.block_rect)

class Maze:
    """
    Setup the maze into four parts.
    """
    def __init__(self, position, maze_map = None):
        self.maze = maze_map
        self.maze_format = []

        # Load block image
        self.wall = pygame.image.load('img/concrete.jpg') 
        self.path = pygame.image.load('img/pathway.JPG') 
        self.portal = pygame.image.load('img/portal.JPG') 

        # Adjust block size
        if len(self.maze) <= 6:
            tile = 50
        elif len(self.maze) <= 10:
            tile = 40
        elif len(self.maze) <= 20:
            tile = 30
        elif len(self.maze) <= 33:
            tile = 15
        else: 
            tile = 10

        row_count = 0
        for row in maze_map:
            col_count = 0
            for block in row:
                if block == 0:
                    b = Block(self.wall, tile, col_count, row_count, position)
                    self.maze_format.append(b.give())
                elif block == 7:
                    b = Block(self.path, tile, col_count, row_count, position)
                    self.maze_format.append(b.give())
                elif block == 8:
                    b = Block(self.portal, tile, col_count, row_count, position)
                    self.maze_format.append(b.give())
                col_count += 1
            row_count += 1
                

    def draw(self, win):
        for block in self.maze_format:
            win.blit(block[0], block[1])

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

class Setup:
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

        # Default variables to what page should be running
        self.main_page = True
        self.instruction_page = False
        self.game_page = False
        self.difficulty_page = False

        # Game background
        self.hell_bg = pygame.image.load('img\hell.jpg')
        self.hell_bg_resized = pygame.transform.scale(self.hell_bg, (self.screen_width, self.screen_height))

        # Button parameters
        self.b_height = 120
        self.b_width = 220
        self.b_x = (self.screen_width - self.b_width) // 2
        self.b_color = (79, 6, 6)

        # Buttons and placement in screen
        self.start_button = button(x=self.b_x, y=200, width=self.b_width, height=self.b_height, color=self.b_color, name="Escape") # start button
        self.instruction_button = button(x=self.b_x, y=350, width=self.b_width, height=self.b_height, color=self.b_color, name="Instruction") # instruction button
        self.back_button = button(x=self.b_x, y=350, width=self.b_width, height=self.b_height, color=self.b_color, name="Back") # back button
        self.easy_button = button(x=500, y=250, width=self.b_width, height=self.b_height, color=self.b_color, name="easy") # easy button
        self.medium_button = button(x=1040, y=250, width=self.b_width, height=self.b_height, color=self.b_color, name="medium") # medium button
        self.hard_button = button(x=500, y=400, width=self.b_width, height=self.b_height, color=self.b_color, name="hard") # hard button
        self.god_button = button(x=1040, y=400, width=self.b_width, height=self.b_height, color=self.b_color, name="god") # god button
        self.custom_button = button(x=self.b_x, y=550, width=self.b_width, height=self.b_height, color=self.b_color, name="custom") # custom button
        self.back_m_button = button(x=self.b_x, y=700, width=self.b_width, height=self.b_height, color=self.b_color, name="back") # back to main button
        self.quit_button = button(x=1450, y=50, width=75, height=30, color=self.b_color, name="quit") # quit button

        # Default Maze map
        self.maze_maam = None

        # Maze positions
        self.pos = []

    def run(self):
        while self.running:
            # Show the background and design (Take note that the order matters to show all images)
            self.screen.blit(self.hell_bg_resized, (0,0))

            # show the elements depending on the page
            if self.game_page:
                self.maze_maam.draw(self.screen)
                self.quit_button.draw(self.screen, (18, 1, 1), 30)
            elif self.main_page:
                self.start_button.draw(self.screen, (18, 1, 1), 60)
                self.instruction_button.draw(self.screen, (18, 1, 1),42)
            elif self.instruction_page:
                self.start_button.draw(self.screen, (18, 1, 1), 60)
                self.back_button.draw(self.screen, (18, 1, 1), 60) 
            elif self.difficulty_page:
                self.easy_button.draw(self.screen, (18, 1, 1), 60) 
                self.medium_button.draw(self.screen, (18, 1, 1), 60) 
                self.hard_button.draw(self.screen, (18, 1, 1), 60) 
                self.god_button.draw(self.screen, (18, 1, 1), 60) 
                self.custom_button.draw(self.screen, (18, 1, 1), 60) 
                self.back_m_button.draw(self.screen, (18, 1, 1), 60) 

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

            # If the game is closed
            if event.type == pygame.QUIT:
                self.running = False

            # Check the events in the game page            
            if self.game_page:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.is_over(pos):
                        print('quit button clicked')
                        self.game_page = False
                        self.main_page = True

                if event.type == pygame.MOUSEMOTION:
                    if self.quit_button.is_over(pos):
                        self.quit_button.color = (38, 3, 3)
                    else:
                        self.quit_button.color = self.b_color

            # Check the events in the main page
            elif self.main_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        print('start button clicked')
                        self.main_page = False
                        self.difficulty_page = True
                    if self.instruction_button.is_over(pos):
                        print('instruction button clicked')
                        self.main_page = False
                        self.instruction_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (38, 3, 3)
                    else:
                        self.start_button.color = self.b_color

                    if self.instruction_button.is_over(pos):
                        self.instruction_button.color = (38, 3, 3)
                    else:
                        self.instruction_button.color = self.b_color

            # Check the events in the difficulty page
            elif self.difficulty_page:
                # If the mouse is click check through all possible difficulty level
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_button.is_over(pos):
                        print('easy button clicked')
                        self.maze_maam = Maze(200, map.easy)
                        self.difficulty_page = False
                        self.game_page = True
                    elif self.medium_button.is_over(pos):
                        print('medium button clicked')
                        self.maze_maam = Maze(200, map.medium)
                        self.difficulty_page = False
                        self.game_page = True
                    elif self.hard_button.is_over(pos):
                        print('hard button clicked')
                        self.maze_maam = Maze(200, map.hard)
                        self.difficulty_page = False
                        self.game_page = True
                    elif self.god_button.is_over(pos):
                        print('god button clicked')
                        self.maze_maam = Maze(200, map.god)
                        self.difficulty_page = False
                        self.game_page = True
                    elif self.custom_button.is_over(pos):
                        print('custom button clicked')
                        self.maze = Maze(200, map.custom)
                        self.difficulty_page = False
                        self.game_page = True
                    elif self.back_m_button.is_over(pos):
                        print('back button clicked')
                        self.difficulty_page = False
                        self.main_page = True
                        

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.easy_button.is_over(pos):
                        self.easy_button.color = (38, 3, 3)
                    else:
                        self.easy_button.color = self.b_color

                    if self.medium_button.is_over(pos):
                        self.medium_button.color = (38, 3, 3)
                    else:
                        self.medium_button.color = self.b_color
            
                    if self.hard_button.is_over(pos):
                        self.hard_button.color = (38, 3, 3)
                    else:
                        self.hard_button.color = self.b_color
            
                    if self.god_button.is_over(pos):
                        self.god_button.color = (38, 3, 3)
                    else:
                        self.god_button.color = self.b_color

                    if self.custom_button.is_over(pos):
                        self.custom_button.color = (38, 3, 3)
                    else:
                        self.custom_button.color = self.b_color
            
                    if self.back_m_button.is_over(pos):
                        self.back_m_button.color = (38, 3, 3)
                    else:
                        self.back_m_button.color = self.b_color
            
            # Check the events in the instruction page
            elif self.instruction_page:
                # If the mouse is click check through all possible pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_over(pos):
                        print('start button clicked')
                        self.instruction_page = False
                        self.difficulty_page = True
                    if self.back_button.is_over(pos):
                        print('back button clicked')
                        self.instruction_page = False
                        self.main_page = True

                # If the mouse is hovered over a button
                if event.type == pygame.MOUSEMOTION:
                    if self.start_button.is_over(pos):
                        self.start_button.color = (38, 3, 3)
                    else:
                        self.start_button.color = self.b_color

                    if self.instruction_button.is_over(pos):
                        self.instruction_button.color = (38, 3, 3)
                    else:
                        self.instruction_button.color = self.b_color