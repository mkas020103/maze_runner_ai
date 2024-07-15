#FILE powerup.py
import pygame
import random
 
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

class Violet:
	def __init__(self, all_path, power_up):
		self.all_path = all_path
		self.power_up = power_up
		self.pos = (self.power_up[1][0], self.power_up[1][1])

	def maam_power(self):
		pass
	
	def ai_power(self):
		pass


class Blue:
	def __init__(self, all_path, power_up):
		self.all_path = all_path
		self.power_up = power_up
		self.pos = (self.power_up[1][0], self.power_up[1][1])

	def move_closer(self):
		pass