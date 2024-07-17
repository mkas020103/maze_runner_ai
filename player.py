import pygame
from pygame.locals import *
import numpy as np
from collections import deque


class Player:
    """
    Player object that moves around the maze

    init:
        self.player_img = a pygame image value
        self.player_rec = a rectangle shape 
        self.explored = list of all explored paths [(x,y) ,(x,y), ...]
        self.unexplored = list of all unexplored paths [(x,y) ,(x,y), ...]
        self.can_explore = list of all exploreable paths [(x,y) ,(x,y), ...]
    """
    def __init__(self, p_size, starting_places, unexplored_path, portal):
        self.portal = (portal[0][0][1][0], portal[0][0][1][1])
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

        self.update_path(current_pos, block_size)
        return True
    
    def update_path(self, current_pos, block_size):
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
    
class A_agent():
    """
    A* algorithm in finding the shortest path

    variables:
        self.block_size = block size (int)
        self.agent = image of the agent <Surface(width x height x depth)>
        self.agent_rect = the box or rectangle position of the agent (<rect(x pos, y pos, width, height)>)
        self.current_pos = the updating position on the agent (int)
        self.portal = np array of one portal [[x y]]
        self.explored = list of paths that are already explored [(x,y), (x,y)]
        self.can_explore = list of path that can be still be explored [(x,y), (x,y)]
        self.start = np array of all starting point [[x y] [x y]]
        self.is_first = number of moves (int)
        self.total_cost_dict = dictionary of position with its cost {(x,y):cost, (x,y):cost} 
    """
    def __init__(self, p_size, starting_place, unexplored_path, portal):
        self.block_size = p_size
        self.agent = pygame.image.load('img/demon.png')
        self.agent = pygame.transform.scale(self.agent, (p_size, p_size))
        self.agent_rect = self.agent.get_rect()
        self.current_pos = None
        self.portal = np.array([(pos[1][0], pos[1][1]) for pos, type in portal])
        self.for_blue_portal = portal
        self.explored = []
        self.unexplored = np.array([(pos[1][0], pos[1][1]) for pos, type in unexplored_path])
        self.can_explore = []
        self.start = np.array([(pos[0], pos[1]) for img, pos in starting_place])
        self.is_first = 0
        self.found_portal = None
        
        # Calculate the Manhattan distance or distance between the goal and each path (h)
        self.manhattan = np.abs(self.unexplored[:, 0] - self.portal[0][0]) + np.abs(self.unexplored[:, 1] - self.portal[0][1])

        self.manhattan_dict = {tuple(path): cost for path, cost in zip(self.unexplored, self.manhattan)}
        
        # Calculate the cost of each tile from the starting point (g)
        self.cost = np.abs(self.unexplored[:, 0] - self.start[0][0]) + np.abs(self.unexplored[:, 1] - self.start[0][1])
        
        # Calculate the total estimated cost (f)
        self.total_cost = self.cost + self.manhattan

        # Dictionary of the unexplored path with its respective value
        self.total_cost_dict = {tuple(path): cost for path, cost in zip(self.unexplored, self.total_cost)}
        
    def best_move(self):
        self.is_first += 1
        if self.is_first != 1:
            # Portal already found
            if self.found_portal:
                return self.found_portal

            # Find the tuple with the minimum cost in explorable paths
            minimum_cost_path, minimum_cost_value = min(self.can_explore, key=lambda x: x[1])
            self.current_pos = minimum_cost_path

            # Remove the current path from can explore, unexplored, and append to explored path
            del self.total_cost_dict[minimum_cost_path]
            self.can_explore.remove((minimum_cost_path,minimum_cost_value))
            self.explored.append(minimum_cost_path)

            # Calculate the adjacent tile
            adjacent_tile = np.array([(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)])

            # If the portal is one of the adjacent tile
            for tile in adjacent_tile:
                if tuple(tile) == tuple(self.portal[0]):
                    self.found_portal = tuple(tile)
                
            # Add the adjacent tile to the can_explore
            adjacent_paths = [(tuple(adj), self.total_cost_dict[tuple(adj)]) for adj in adjacent_tile if tuple(adj) in self.total_cost_dict]
            for path in adjacent_paths:
                if path not in self.can_explore:
                    self.can_explore.append(path)

            return minimum_cost_path
            
        else:
            # Set the starting point
            self.current_pos = self.start[0]

             # Calculate the adjacent tile
            adjacent_tile = np.array([(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)])
            
            # If the portal is one of the adjacent tile
            for tile in adjacent_tile:
                if tuple(tile) == tuple(self.portal[0]):
                    self.found_portal = tuple(tile)

            # Add the adjacent tile to the can_explore
            adjacent_paths = [(tuple(adj), self.total_cost_dict[tuple(adj)]) for adj in adjacent_tile if tuple(adj) in self.total_cost_dict]
            for path in adjacent_paths:
                if path not in self.can_explore:
                    self.can_explore.append(path)

            # Update the unexplored and explored part
            del self.total_cost_dict[tuple(self.start[0])]
            self.explored.append(tuple(self.start[0]))
            return tuple(self.start[0])
        
    def update_path(self, current_pos):
        self.current_pos = current_pos

        # Calculate the adjacent tile
        adjacent_tile = np.array([(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                        (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)])
        
        # Add the adjacent tile to the can_explore
        adjacent_paths = [(tuple(adj), self.total_cost_dict[tuple(adj)]) for adj in adjacent_tile if tuple(adj) in self.total_cost_dict]
        for path in adjacent_paths:
            if path not in self.can_explore:
                self.can_explore.append(path)

        for tile in adjacent_tile:
            if tuple(tile) == tuple(self.portal[0]):
                self.found_portal = tuple(tile)

        
    def draw(self, win, pos):
        self.agent_rect.x = pos[0]
        self.agent_rect.y = pos[1]
        win.blit(self.agent, self.agent_rect)


class DFS_agent(Player):
    """
    DFS algorithm in finding the shortest path

    variables:
        self.block_size = block size (int)
        self.agent = image of the agent <Surface(width x height x depth)>
        self.agent_rect = the box or rectangle position of the agent (<rect(x pos, y pos, width, height)>)
        self.current_pos = the updating position on the agent (int)
        self.portal = tuple containing the x and y coords of the portal
        self.explored = list of paths that are already explored [(x,y), (x,y)]
        self.can_explore = list of path that can be still be explored [(x,y), (x,y)]
        self.start = np array of all starting point [[x y] [x y]]
        self.is_first = number of moves (int)
        self.found_portal = variable in determining whether the portal is already found 
    """
    def __init__(self, p_size, starting_places, unexplored_path, portal):
        super().__init__(p_size, starting_places, unexplored_path, portal)
        self.block_size = p_size
        self.agent = pygame.image.load('img/demon.png')
        self.agent = pygame.transform.scale(self.agent, (p_size, p_size))
        self.agent_rect = self.agent.get_rect()
        self.unexplored = [(pos[1][0], pos[1][1]) for pos, type in unexplored_path]
        self.start = np.array([(pos[0], pos[1]) for img, pos in starting_places])
        self.portal = (portal[0][0][1][0], portal[0][0][1][1])
        self.is_first = 0
        self.explored = []
        self.can_explore = []
        self.current_pos = None
        self.found_portal = False

    def move(self):
        self.is_first += 1
        if self.is_first != 1:
            if self.found_portal:
                return self.portal
            # Get the deepest place 
            self.current_pos = self.can_explore[-1]

            # Remove the current move in the explorable
            self.can_explore.pop()

            # Calculate the adjacent tile
            adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

            # Update the explorable and unexplored path
            adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
            for path in adjacent_paths:
                if path not in self.can_explore:
                    self.can_explore.append(path)

            self.unexplored = [path for path in self.unexplored if path not in adjacent_paths]

            # If portal already found just return the portal
            if self.portal in adjacent_tile:
                self.found_portal = True

            # Return the deepest move
            return self.current_pos
        else:
            # Set the starting point
            self.current_pos = self.start[0]
            # Calculate the adjacent tile
            adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

            # Add the adjacent tile to the can_explore
            adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
            for path in adjacent_paths:
                if path not in self.can_explore:
                    self.can_explore.append(path)

            # Update the unexplored and explored part
            self.unexplored.remove(tuple(self.start[0]))
            self.explored.append(tuple(self.start[0]))

            # If portal already found just return the portal
            if self.portal in adjacent_tile:
                self.found_portal = True

            return tuple(self.start[0])
    
    def update_path(self, current_pos):
        self.current_pos = current_pos

        # Calculate the adjacent tile
        adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                        (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

        # Add the adjacent tile to the can_explore
        adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
        for path in adjacent_paths:
            if path not in self.can_explore:
                self.can_explore.append(path)

        # If portal already found just return the portal
        if self.portal in adjacent_tile:
            self.found_portal = True
        
        # If the current position is still not already explored remove it from the list
        if self.current_pos in self.unexplored:
            self.unexplored.remove(self.current_pos)

    def draw(self, win, pos):
        self.agent_rect.x = pos[0]
        self.agent_rect.y = pos[1]
        win.blit(self.agent, self.agent_rect)

class BFS_agent(Player):
    """
    BFS algorithm in finding the shortest path

    variables:
        self.block_size = block size (int)
        self.agent = image of the agent <Surface(width x height x depth)>
        self.agent_rect = the box or rectangle position of the agent (<rect(x pos, y pos, width, height)>)
        self.current_pos = the updating position on the agent (int)
        self.portal = tuple containing the x and y coords of the portal
        self.explored = list of paths that are already explored [(x,y), (x,y)]
        self.can_explore = list of path that can be still be explored [(x,y), (x,y)]
        self.start = np array of all starting point [[x y] [x y]]
        self.is_first = number of moves (int)
        self.found_portal = variable in determining whether the portal is already found 
    """
    def __init__(self, p_size, starting_places, unexplored_path, portal):
        super().__init__(p_size, starting_places, unexplored_path, portal)
        self.block_size = p_size
        self.agent = pygame.image.load('img/demon.png')
        self.agent = pygame.transform.scale(self.agent, (p_size, p_size))
        self.agent_rect = self.agent.get_rect()
        self.unexplored = [(pos[1][0], pos[1][1]) for pos, type in unexplored_path]
        self.start = np.array([(pos[0], pos[1]) for img, pos in starting_places])
        self.portal = (portal[0][0][1][0], portal[0][0][1][1])
        self.is_first = 0
        self.explored = []
        self.can_explore = []
        self.current_pos = None
        self.found_portal = False

    def move(self):
        self.is_first += 1
        if self.is_first != 1:
            if self.found_portal:
                return self.portal
            # Get the breath place 
            self.current_pos = self.can_explore[0]
            
            # Remove the current move in the explorable
            self.can_explore.pop(0)

            # Calculate the adjacent tile
            adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

            # Update the explorable and unexplored path
            adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
            for path in adjacent_paths:
                if path not in self.can_explore and path in self.unexplored:
                    self.can_explore.append(path)

            self.unexplored = [path for path in self.unexplored if path not in adjacent_paths]

            # If portal already found just return the portal
            if self.portal in adjacent_tile:
                self.found_portal = True

            # Return the deepest move
            return self.current_pos
        else:
            # Set the starting point
            self.current_pos = self.start[0]
            # Calculate the adjacent tile
            adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                         (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

            # Add the adjacent tile to the can_explore
            adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
            for path in adjacent_paths:
                if path not in self.can_explore:
                    self.can_explore.append(path)

            # Update the unexplored and explored part
            self.unexplored.remove(tuple(self.start[0]))
            self.explored.append(tuple(self.start[0]))

            # If portal already found just return the portal
            if self.portal in adjacent_tile:
                self.found_portal = True

            return tuple(self.start[0])
    
    def update_path(self, current_pos):
        self.current_pos = current_pos

        # Calculate the adjacent tile
        adjacent_tile = [(self.current_pos[0], self.current_pos[1] - self.block_size), (self.current_pos[0] - self.block_size, self.current_pos[1]), 
                        (self.current_pos[0] + self.block_size, self.current_pos[1]), (self.current_pos[0], self.current_pos[1] + self.block_size)]

        # Add the adjacent tile to the can_explore
        adjacent_paths = [adj for adj in adjacent_tile if adj in self.unexplored]
        for path in adjacent_paths:
            if path not in self.can_explore:
                self.can_explore.append(path)

        # If portal already found just return the portal
        if self.portal in adjacent_tile:
            self.found_portal = True
        
        # If the current position is still not already explored remove it from the list
        if self.current_pos in self.unexplored:
            self.unexplored.remove(self.current_pos)

    def draw(self, win, pos):
        self.agent_rect.x = pos[0]
        self.agent_rect.y = pos[1]
        win.blit(self.agent, self.agent_rect)
        