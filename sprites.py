import pygame
from pygame.locals import *

class Block:
    """
    Block that build up the maze (i.e. path, portal, powerup, wall)
    """
    def __init__(self, block_image, tile, col, row, xposition, yposition):
        self.tile_size = tile
        # Transform the image size
        self.block = pygame.transform.scale(block_image, (self.tile_size, self.tile_size))
        # makes the image a "rectangle" object of pygame
        self.block_rect = self.block.get_rect()
        # Plot the x and y coordinates of the image
        self.block_rect.x = col * self.tile_size + xposition
        self.block_rect.y = row * self.tile_size + yposition

    def give(self):
        return (self.block, self.block_rect)

class Maze:
    """
    Setup the maze into four parts.
    """
    def __init__(self, xposition, yposition, maze_map = None):
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
        elif len(self.maze) <= 14:
            tile = 30
        elif len(self.maze) <= 20:
            tile = 22
        else: 
            tile = 10

        row_count = 0
        for row in maze_map:
            col_count = 0
            for block in row:
                if block == 0:
                    b = Block(self.wall, tile, col_count, row_count, xposition, yposition)
                    self.maze_format.append(b.give())
                elif block == 7:
                    b = Block(self.path, tile, col_count, row_count, xposition,yposition)
                    self.maze_format.append(b.give())
                elif block == 8:
                    b = Block(self.portal, tile, col_count, row_count, xposition, yposition)
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
    
class Font:
    # Render the text
    def __init__(self, text, pos):
        font = pygame.font.Font(None, 74) 
        self.text_color = (255, 255, 255)
        self.text_surface = font.render(text, True, self.text_color)

        # Position the text
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = pos

    def draw(self, win):
        win.blit(self.text_surface, self.text_rect)