import pygame as pg
from pygame import Vector2, Vector3
import Config

import UITEMS.Box


class Bitmap:
	@staticmethod
	def loadBitmap(filename="../Bitmaps/save.bm"):
		try:
			with open(filename, mode="r+") as file:
				bitmap = eval(file.readline().replace("\n", ""))

			return bitmap
		except FileNotFoundError:
			print("File Not Found")
			return [""]


	def __init__(self, pos=None):
		self.pos = pos
		self.currentFrame = 0
		self.currentAnimation = "default"
		self.timer = 0

		self.animations = {"default": {"frameTime": 1, "frames": []}}

	def update(self, parent):
		self.timer += parent.app.clock.get_time() / 1000

		frameTime = self.animations[self.currentAnimation]["frameTime"]
		if self.timer > frameTime:
			framesSkipped = int(self.timer // frameTime)
			self.timer %= frameTime

			for _ in range(framesSkipped):
				self.nextFrame()

	def render(self, parent):
		if self.currentAnimation not in self.animations.keys():
			return -1
		if self.currentFrame >= len(self.animations[self.currentAnimation]["frames"]):
			return -1

		pos = self.pos
		if pos is None:
			pos = parent.pos

		for y, row in enumerate(self.animations[self.currentAnimation]["frames"][self.currentFrame]):
			for x, state in enumerate(row):
				if state in ["0", 0]:
					continue

				pg.draw.rect(parent.app.screen, (255, 255, 255),
							 pg.Rect((pos + Vector2(x, y)) * Config.PIXEL_SIZE,
									 (Config.PIXEL_SIZE, Config.PIXEL_SIZE)))


	def addAnimation(self, name):
		self.animations[name] = [[""]]

	def removeAnimation(self, name):
		self.animations.pop(name)

	def addNewFrame(self, animationName, bitmapFrame=[""]):
		self.animations[animationName]["frames"].append(bitmapFrame)

	def removeFrame(self, animationName, frameNumber):
		self.animations[animationName]["frames"].pop(frameNumber)

	def nextFrame(self):
		if len(self.animations[self.currentAnimation]["frames"]) == 0:
			return -1

		self.currentFrame = (self.currentFrame + 1) % len(self.animations[self.currentAnimation]["frames"])

	def prevFrame(self):
		self.currentFrame = (self.currentFrame - 1) % len(self.animations[self.currentFrame]["frames"])


	def setCurrentFrame(self, frame):
		self.currentFrame = frame % len(self.animations[self.currentAnimation]["frames"])

	def setCurrentAnimation(self, animationName):
		if animationName not in self.animations.keys():
			return -1
		self.currentAnimation = animationName

		return 0

	def setAnimationFrameTime(self, frameTime):
		self.animations[self.currentAnimation]["frameTime"] = frameTime


	def getCurrentAnimationName(self):
		return self.currentAnimation

	def getCurrentFrameNumber(self):
		return self.currentFrame

	def getCurrentAnimation(self):
		return self.animations[self.currentAnimation]

	def getCurrentFrame(self):
		return self.animations[self.currentAnimation]["frames"][self.currentFrame]

	def getCurrentFrameTime(self):
		return self.animations[self.currentAnimation]["frameTime"]




class Image(UITEMS.Box.Box):
	def __init__(self, app, pos=Vector2(0, 0), bitmapFile="Bitmaps/Cursor.bm"):
		super().__init__(app, pos, Vector2(0, 0))

		self.bitmap = Bitmap()
		if bitmapFile is not None:
			self.bitmap.addNewFrame("default", Bitmap.loadBitmap(bitmapFile))

	def update(self):
		self.bitmap.update(self)

	def render(self):
		self.bitmap.render(self)