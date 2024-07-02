import pygame
from pygame.locals import *
from player import *

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
    def __init__(self, xposition, yposition, maze_map, custom_size):
        self.maze = maze_map
        self.wall_format = []
        self.path_format = []
        self.portal_format = []
        self.positions = []

        # Load block image
        self.wall = pygame.image.load('img/concrete.jpg') 
        self.path = pygame.image.load('img/pathway.JPG') 
        self.portal = pygame.image.load('img/portal.JPG') 

        # Adjust block size
        if custom_size != None:
            self.tile = custom_size
        else:
            if len(self.maze) <= 6:
                self.tile = 50
            elif len(self.maze) <= 10:
                self.tile = 40
            elif len(self.maze) <= 14:
                self.tile = 30
            elif len(self.maze) <= 20:
                self.tile = 20
            else: 
                self.tile = 10

        row_count = 0
        # Add the type of block on a specific screen position
        for row in maze_map:
            col_count = 0
            for block in row:
                if block == 0:
                    b = Block(self.wall, self.tile, col_count, row_count, xposition, yposition)
                    self.wall_format.append([b.give(),'w'])
                    self.positions.append([b.give(),'w'])
                elif block == 7:
                    b = Block(self.path, self.tile, col_count, row_count, xposition,yposition)
                    self.path_format.append([b.give(),'p'])
                    self.positions.append([b.give(),'p'])
                elif block == 8:
                    b = Block(self.portal, self.tile, col_count, row_count, xposition, yposition)
                    self.portal_format.append([b.give(),'l'])
                    self.positions.append([b.give(),'l'])
                col_count += 1
            row_count += 1

    def position(self):
        return self.positions
                

    def draw(self, win):
        # draw the walls, path, and portal
        for wall in self.wall_format:
            win.blit(wall[0][0], wall[0][1])
        for path in self.path_format:
            win.blit(path[0][0], path[0][1])
        for portal in self.portal_format:
            win.blit(portal[0][0], portal[0][1])

class Smoke:
    """
    Smoke that covers the map
    """
    def __init__(self, map_to_cover, fog_size, path_format, fog_adjustment):
        self.cover = map_to_cover
        self.path = path_format
        self.smoke_list = []

        # Get the starting places
        self.starting_places = []
        self.find_starting_pos()

        # Load image
        self.smoke = pygame.image.load('img/fog.png')

        # Transform the image size
        self.smoke = pygame.transform.scale(self.smoke, (fog_size + fog_adjustment, fog_size + fog_adjustment)) # 47 best size

        # Calculate the offset to keep the smoke centered
        self.offset = (fog_size + fog_adjustment - fog_size) // 2  # 47 best size
    
        for fog_pos, type in map_to_cover:
            if fog_pos not in self.starting_places:
                # Make the image a "rectangle" object of pygame
                smoke_rect = self.smoke.get_rect()
                # Plot the x and y coordinates of the image
                smoke_rect.x = fog_pos[1][0] - self.offset
                smoke_rect.y = fog_pos[1][1] - self.offset
                self.smoke_list.append((self.smoke, smoke_rect))

    def find_starting_pos(self):
        # Initialize variables to store edge coordinates
        min_x = float('inf')
        max_x = float('-inf')
        min_y = float('inf')
        max_y = float('-inf')
        most_left = float('inf')
        most_right = float('-inf')

        unique = []
        row = 1

        # Find the min and max x and y values
        for coord, type in self.cover:
            if coord[1][0] < most_left:
                most_left = coord[1][0]
            if coord[1][0] > most_right:
                most_right = coord[1][0]

            if coord[1][0] < min_x and type == 'p':
                min_x = coord[1][0]
            if coord[1][0] > max_x and type == 'p':
                max_x = coord[1][0]
            if coord[1][1] < min_y and type == 'p':
                min_y = coord[1][1]
            if coord[1][1] > max_y and type == 'p':
                max_y = coord[1][1]
            if coord[1][1] not in unique:
                unique.append((coord[1][1]))

        row_len = len(unique)
        current_row = 0
        row_value = 0
        # Collect the tuples that are at the edges #self.starting_places.append(coord)
        for coord, type in self.path:
            if coord[1][1] != row_value:
                row_value = coord[1][1]
                current_row += 1

            # Find the starting points found on the maze edges
            if current_row == 1:
                if coord[1][1] == min_y:
                    self.starting_places.append(coord)
            elif current_row == row_len:
                if coord[1][1] == max_y:
                    self.starting_places.append(coord)
            else:
                if (coord[1][0] == min_x or coord[1][0] == max_x) and (coord[1][0] == most_left or coord[1][0] == most_right):
                    self.starting_places.append(coord)

    def draw(self, win):
        for smoke in self.smoke_list:
            win.blit(smoke[0], smoke[1])

    def remove_adjacent_smokes(self, player_pos, block_size):
        # Calculate the adjacent fogs
        padding_ul = block_size + self.offset
        padding_rd = block_size - self.offset
        adjacent_fogs = [
            (player_pos[0] + padding_rd, player_pos[1] - block_size + padding_rd),     # Right
            (player_pos[0] - block_size + padding_rd, player_pos[1] + padding_rd),     # Down
            (player_pos[0] + block_size - padding_ul, player_pos[1] - padding_ul),     # Up
            (player_pos[0] - padding_ul, player_pos[1] + block_size - padding_ul)      # Left
        ]
        # Update smoke_list, removing adjacent fogs
        self.smoke_list = [unremoved_block for unremoved_block in self.smoke_list if (unremoved_block[1][0],unremoved_block[1][1]) not in adjacent_fogs]
    
class mode:
    """
    The font, maze, player, and fog settings of each mode
    """
    def __init__(self, font_list, maze_list, fog_adjustment, custom_map_size=None):
        # Font setting
        self.d1 = Font(font_list[0][0], font_list[0][1])
        self.d2 = Font(font_list[1][0], font_list[1][1])
        self.d3 = Font(font_list[2][0], font_list[2][1])

        # Maze setting
        self.maze_bfs = Maze(maze_list[0][0], maze_list[0][1], maze_list[0][2], custom_map_size)
        self.maze_dfs = Maze(maze_list[1][0], maze_list[1][1], maze_list[1][2], custom_map_size)
        self.maze_maam = Maze(maze_list[2][0], maze_list[2][1], maze_list[2][2], custom_map_size)
        self.maze_a = Maze(maze_list[3][0], maze_list[3][1], maze_list[3][2], custom_map_size)

        # Fog setting
        self.fog_bfs = Smoke(self.maze_bfs.position(), self.maze_bfs.tile, self.maze_bfs.path_format, fog_adjustment)
        self.fog_dfs = Smoke(self.maze_dfs.position(), self.maze_dfs.tile, self.maze_dfs.path_format, fog_adjustment)
        self.fog_a = Smoke(self.maze_a.position(), self.maze_a.tile, self.maze_a.path_format, fog_adjustment)
        self.fog_maam = Smoke(self.maze_maam.position(), self.maze_maam.tile, self.maze_maam.path_format, fog_adjustment)

        # Player setting
        self.player = Player(self.maze_maam.tile, self.fog_maam.starting_places, self.maze_maam.path_format)

        # agent player setting
        #self.bfs_agent = BFS_agent(self.maze_a.tile, self.fog_a.starting_places, self.maze_a.path_format)
        #self.dfs_agent = DFS_agent(self.maze_a.tile, self.fog_a.starting_places, self.maze_a.path_format)
        self.a_agent = A_agent(self.maze_a.tile, self.fog_a.starting_places, self.maze_a.path_format, self.maze_a.portal_format)

    def draw(self, win):
        # Draw maze
        self.maze_maam.draw(win)
        self.maze_dfs.draw(win)
        self.maze_bfs.draw(win)
        self.maze_a.draw(win)

        # Draw text
        self.d1.draw(win)
        self.d2.draw(win)
        self.d3.draw(win)

        # Draw fog
        self.fog_bfs.draw(win)
        self.fog_dfs.draw(win)
        self.fog_a.draw(win)
        self.fog_maam.draw(win)

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
            font = pygame.font.SysFont('franklingothicmedium', fsize)
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
        font = pygame.font.SysFont('calibri', 74) 
        self.text_color = (255, 255, 255)
        self.text_surface = font.render(text, True, self.text_color)

        # Position the text
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = pos

    def draw(self, win):
        win.blit(self.text_surface, self.text_rect)