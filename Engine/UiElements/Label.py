from Engine.UiElements import Box, Bitmap
from Engine.FontOperator import *


class Label(Box.Box):
	"""
	Basic text Label. Contains many Bitmap objects to every letter in given text
	"""

	def __init__(self, app, pos=Vector2(0, 0), font=None, text="abcdefg"):
		super().__init__(app, pos=pos)

		if font is None:
			font = "FONT_4X5"

		self.font = font
		self.text = text
		self.bitmap = Bitmap.Bitmap()
		self.generateNewBitmapText()

	def generateNewBitmapText(self):
		"""
		Generates Bitmap list by self.text with given font
		:return:
		"""
		fontInfo = getFontInfo(fontName=self.font)
		if fontInfo == -1:
			return -1

		bitmapText = [getCharBitmapList(self.font, char) for char in self.text]
		bitmapList = bitmapText[0]

		for item in bitmapText[1:]:
			for index, row in enumerate(item):
				bitmapList[index] += row

		self.bitmap = Bitmap.Bitmap()
		self.bitmap.addNewFrame("default", bitmapList)

	def update(self):
		"""
		Updates every Bitmap object
		:return:
		"""
		self.bitmap.update(self)

	def render(self):
		"""
		Renders every Bitmap object
		:return:
		"""
		self.bitmap.render(self)