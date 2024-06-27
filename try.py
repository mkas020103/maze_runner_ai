import numpy as np

class A_agent():
    def __init__(self, starting_place, unexplored_path, portal):
        self.step = None
        self.portal = np.array([(pos[1][0], pos[1][1]) for pos, type in unexplored_path])
        self.explored = []
        self.unexplored = np.array([(pos[1][0], pos[1][1]) for pos, type in unexplored_path])
        self.start = np.array([(pos[0], pos[1]) for img, pos in starting_place])
        
        # Calculate the Manhattan distance or distance between the goal and each path (h)
        self.manhattan = np.abs(self.unexplored[:, 0] - self.portal[0][0]) + np.abs(self.unexplored[:, 1] - self.portal[0][1])
        
        # Calculate the cost of each tile from the starting point (g)
        self.cost = np.abs(self.unexplored[:, 0] - self.start[0][0]) + np.abs(self.unexplored[:, 1] - self.start[0][1])
        
        # Calculate the total estimated cost (f)
        self.total_cost = self.cost + self.manhattan
        
        print('Unexplored paths:', self.unexplored)
        print('Manhattan distances:', self.manhattan)
        print('Initial costs (g-values):', self.cost)
        print('Total estimated cost (f-values):', self.total_cost)

# Example usage
starting_place = [((0, 0), (1, 1))]
unexplored_path = [((0, 0), (2, 2)), ((0, 0), (3, 3)), ((0, 0), (4, 4))]
portal = [((0, 0), (5, 5))]

agent = A_agent(starting_place, unexplored_path, portal)
