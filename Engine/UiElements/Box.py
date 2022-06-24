import pygame as pg
from pygame import Vector2
from Engine import Config

class Box:
	"""
	Basic box ui element that will do nothing except of be drawn on screen
	Make rectangle by setting size. It'll be filled by completely white color
	"""

	def __init__(self, app, pos=Vector2(0, 0), size=Vector2(16, 16)):
		self.app = app
		self.pos = pos
		self.size = size

	def update(self):
		pass

	def render(self):
		pg.draw.rect(self.app.screen, (255, 255, 255),
					 pg.Rect(self.pos * Config.PIXEL_SIZE, self.size * Config.PIXEL_SIZE))