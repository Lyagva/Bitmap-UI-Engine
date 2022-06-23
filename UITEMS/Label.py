import pygame as pg
from pygame import Vector2, Vector3
import Config

import UITEMS.Bitmap
import UITEMS.Box
from FontOperator import *


class Label(UITEMS.Box.Box):
	"""
	Basic text Label. Contains many Bitmap objects to every letter in given text
	"""

	def __init__(self, app, pos=Vector2(0, 0), font="FONT_4X5", text="abcdefg"):
		super().__init__(app, pos=pos)

		self.font = font
		self.text = text
		self.bitmapText = []
		self.generateNewBitmapText()

	def generateNewBitmapText(self):
		"""
		Generates Bitmap list by self.text with given font
		:return:
		"""
		fontInfo = getFontInfo(fontName=self.font)
		if fontInfo == -1:
			return -1

		self.bitmapText = [getBitmap(self.font, char) for char in self.text]

		for index, bitmapItem in enumerate(self.bitmapText):
			bitmapItem.pos = self.pos + Vector2(index * fontInfo["size"].x, 0)

	def update(self):
		"""
		Updates every Bitmap object
		:return:
		"""
		for index, bitmapItem in enumerate(self.bitmapText):
			bitmapItem.update(self)

	def render(self):
		"""
		Renders every Bitmap object
		:return:
		"""
		for index, bitmapItem in enumerate(self.bitmapText):
			bitmapItem.render(self)