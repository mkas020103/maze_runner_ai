import pygame
from pygame.locals import *
from sprites import Maze
import map
class Smoke:
    """
    Smoke that covers the map
    """
    def __init__(self, map_to_cover, fog_size, path_format):
        self.cover = map_to_cover
        self.path = path_format
        self.smoke_list = []

        # Get the starting places
        self.starting_places = []
        self.find_starting_pos()

        # Load image
        self.smoke = pygame.image.load('img/fog.png')

        # Transform the image size
        self.smoke = pygame.transform.scale(self.smoke, (fog_size+46, fog_size+46)) # 46 best size

        # Calculate the offset to keep the smoke centered
        self.offset = (fog_size + 46 - fog_size) // 2  # 47 best size
    
        for fog_pos, type in map_to_cover:
            if fog_pos not in self.starting_places:
                # Make the image a "rectangle" object of pygame
                smoke_rect = self.smoke.get_rect()
                # Plot the x and y coordinates of the image
                smoke_rect.x = fog_pos[1][0] - self.offset
                smoke_rect.y = fog_pos[1][1] - self.offset
                self.smoke_list.append((self.smoke, smoke_rect))


maze_list = [(150, 50, map.medium), (1200, 550,  map.medium), (1200, 50,  map.medium), (150, 550,  map.medium)]
maze_maam = Maze(maze_list[2][0], maze_list[2][1], maze_list[2][2])
fog_maam = Smoke(maze_maam.position(), maze_maam.tile, maze_maam.path_format)