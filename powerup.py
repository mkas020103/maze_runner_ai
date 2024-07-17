#FILE powerup.py
import pygame
import random
import numpy as np
 
class Red:
	def __init__(self, all_path, power_up):
		self.all_path = all_path
		self.power_up = power_up
		self.pos = (self.power_up[1][0], self.power_up[1][1])
	
	def random_add(self):
		random_path = random.choice(self.all_path)
		return (random_path[0][1][0], random_path[0][1][1])
		
	def draw(self, win):
		win.blit(self.power_up[0], self.power_up[1])


class Blue:
	def __init__(self, unexplored, power_up, portal):
		self.power_up = power_up
		self.pos = (self.power_up[1][0], self.power_up[1][1])

		# Distance of each point to the goal
		self.portal = portal
		self.manhattan = np.abs(unexplored[:, 0] - self.portal[0]) + np.abs(unexplored[:, 1] - self.portal[1])

		self.manhattan_dict = {tuple(path): cost for path, cost in zip(unexplored, self.manhattan)}

	def move_closer(self, explorable):
		# Get the paths that are explorable only
		current_paths = [x for x in explorable if x in self.manhattan_dict]
		
		# Return the explorable point with the smallest manhattan value
		best_path = min(current_paths, key=lambda x: self.manhattan_dict[x])

		#print('current paths: ',current_paths)
		#print('best path: ', best_path)
		return best_path

	def draw(self, win):
		win.blit(self.power_up[0], self.power_up[1])

class Violet:
	def __init__(self, power_up):
		self.power_up = power_up
		self.pos = (self.power_up[1][0], self.power_up[1][1])

	def maam_power(self):
		pass
	
	def ai_power(self):
		pass

	def draw(self, win):
		win.blit(self.power_up[0], self.power_up[1])