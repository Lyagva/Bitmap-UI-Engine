import pygame as pg
from pygame import Vector2, Vector3
import Config

class Box:
	def __init__(self, app, pos=Vector2(0, 0), size=Vector2(16, 16)):
		self.app = app
		self.pos = pos
		self.size = size

	def update(self):
		pass

	def render(self):
		pg.draw.rect(self.app.screen, (255, 255, 255),
					 pg.Rect(self.pos * Config.PIXEL_SIZE, self.size * Config.PIXEL_SIZE))