#FILE powerup.py
import pygame
import random
 
class Red:
	def __init__(self, all_path, power_up):
		self.all_path = all_path
		self.power_up = power_up
	
	def random(self):
		random_path = random.choice(self.all_path)
		self.all_path.remove(random_path)
		return random_path
		
	def draw(self, win):
		win.blit(self.power_img, self.power_rect) #TODO: change parameters