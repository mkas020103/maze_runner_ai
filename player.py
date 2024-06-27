import pygame
from pygame.locals import *
import numpy as np

class Player:
    """
    Player object that moves around the maze

    init:
        self.player_img = a pygame image value
        self.player_rec = a rectangle shape 

    """
    def __init__(self, p_size, starting_places, unexplored_path):
        self.player_img = pygame.image.load('img/player.png')
        self.player_img = pygame.transform.scale(self.player_img, (p_size, p_size))
        self.player_rect = self.player_img.get_rect()
        self.explored = []
        self.unexplored = [(pos[1][0], pos[1][1]) for pos, type in unexplored_path] # paths that are unexplored
        self.can_explore = [(pos[0], pos[1]) for img, pos in starting_places] # paths that the player can currently explore

    def draw(self, win, pos):
        self.player_rect.x = pos[0]
        self.player_rect.y = pos[1]
        win.blit(self.player_img, self.player_rect)

    def check_place(self, current_pos, block_size):
        if current_pos in self.explored:
            return False
        if current_pos not in self.can_explore:
            return False

        # Calculate the adjacent tile
        adjacent_tile = [(current_pos[0], current_pos[1] - block_size), (current_pos[0] - block_size, current_pos[1]), 
                         (current_pos[0] + block_size, current_pos[1]), (current_pos[0], current_pos[1] + block_size)]
        
        # iterate over each tile, updating the unexplored to its adjacent path 
        # and adding current tile to the explored path
        for pos in self.unexplored:
            # If an unexplored position is a pathway and is not a path that can already be explored, append to can_explore
            if (pos in adjacent_tile) and (pos not in self.can_explore):
                self.can_explore.append(pos)

        self.explored.append(current_pos)
        return True
    
class A_agent():
    def __init__(self, p_size, starting_place, unexplored_path, portal):
        self.agent = pygame.image.load('img/demon.png')
        self.agent = pygame.transform.scale(self.agent, (p_size, p_size))
        self.agent_rect = self.agent.get_rect()
        self.current_pos = None
        self.portal = np.array([(pos[1][0], pos[1][1]) for pos, type in portal])
        self.explored = []
        self.unexplored = np.array([(pos[1][0], pos[1][1]) for pos, type in unexplored_path])
        self.start = np.array([(pos[0], pos[1]) for img, pos in starting_place])
        self.is_first = 0
        
        # Calculate the Manhattan distance or distance between the goal and each path (h)
        self.manhattan = np.abs(self.unexplored[:, 0] - self.portal[0][0]) + np.abs(self.unexplored[:, 1] - self.portal[0][1])
        
        # Calculate the cost of each tile from the starting point (g)
        self.cost = np.abs(self.unexplored[:, 0] - self.start[0][0]) + np.abs(self.unexplored[:, 1] - self.start[0][1])
        
        # Calculate the total estimated cost (f)
        self.total_cost = self.cost + self.manhattan

        # Dictionary of the unexplored path with its respective value
        self.total_cost_dict = {tuple(path): cost for path, cost in zip(self.unexplored, self.total_cost)}
        
        #print('Unexplored paths:', self.unexplored)
        #print('Manhattan distances:', self.manhattan)
        #print('Initial costs (g-values):', self.cost)
        #print('Total estimated cost (f-values):', self.total_cost)
        #print('Total estimated cost (f-values) Dictionary:', self.total_cost_dict)
        print('starting position: ',self.start)

    def best_move(self):
        self.is_first += 1
        if self.is_first != 1:
            pass
        else:
            self.current_pos = self.start[0]
            return tuple(self.start[0])
        
    def draw(self, win, pos):
        self.agent_rect.x = pos[0]
        self.agent_rect.y = pos[1]
        win.blit(self.agent, self.agent_rect)


class DFS_agent(Player):
    def __init__(self, p_size, starting_places, unexplored_path):
        super().__init__(p_size, starting_places, unexplored_path)
        # TODO

class BFS_agent(Player):
    def __init__(self, p_size, starting_places, unexplored_path):
        super().__init__(p_size, starting_places, unexplored_path)
        # TODO
        