import pygame as pg
from pygame import Vector2, Vector3
import Config

import UITEMS.Bitmap
import UITEMS.Box


def clamp(x, l, r):
	"""
	Clamps x var to given borders
	:param x: var that will be clamped
	:param l: Left border
	:param r: Right border
	:return: clamped var
	"""
	return int(max(min(x, r), l))


class Button(UITEMS.Box.Box):
	"""
	Basic Button ui element, that can be pressed with mouse
	"""

	def __init__(self, app, pos=Vector2(0, 0), bitmapFile="Bitmaps/KeyLeft.bm"):
		super().__init__(app, pos=pos)
		self.bitmap = UITEMS.Bitmap.Bitmap()
		self.bitmap.addNewFrame("default", UITEMS.Bitmap.Bitmap.loadBitmap(bitmapFile))
		self.size = Vector2(max([len(row) for row in self.bitmap.getCurrentFrame()]),
							max([len(self.bitmap.getCurrentFrame())]))


		self.pressed = False

	def update(self):
		"""
		Basic update.
		Updates Bitmap object + calls onClick() function when clicked with mouse and
			onPress() function every frame mouse held on object
		:return:
		"""
		self.bitmap.update(self)

		if pg.mouse.get_pressed(3)[0]:
			mousePos = Vector2(pg.mouse.get_pos()) // Config.PIXEL_SIZE - self.pos

			if (clamp(mousePos.x, 0, self.size.x) == mousePos.x and
					clamp(mousePos.y, 0, self.size.y) == mousePos.y) and not self.pressed:
				self.onClick()
				self.pressed = True
		else:
			self.pressed = False

		if self.pressed:
			self.onPress()

	def onClick(self):
		"""
		Called on mouse firstly clicked
		:return:
		"""
		pass

	def onPress(self):
		"""
		Called every frame mouse holds on this object
		:return:
		"""
		pass

	def render(self):
		"""
		Renders Bitmap object
		:return:
		"""
		self.bitmap.render(self)