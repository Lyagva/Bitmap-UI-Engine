import pygame as pg
from pygame import Vector2, Vector3
import Config

import UITEMS.Box


class Bitmap:
	"""
	Basic bitmap elements. Can be drawn, can have multiple animations, with different amount of frames
	"""

	@staticmethod
	def loadBitmap(filename="../Bitmaps/save.bm"):
		"""
		Static method
		Reads file and returns bitmap list
		:param filename: Name of .bm file
		:return: .bm like list. If file not found, returns [""]
		"""

		try:
			with open(filename, mode="r+") as file:
				bitmap = eval(file.readline().replace("\n", ""))

			return bitmap
		except FileNotFoundError:
			print("File Not Found")
			return [""]


	def __init__(self, pos=None):
		"""
		Init basic Bitmap class
		:param pos: Will be rendered on this position. If not given, will be rendered on Parent's position
		"""

		self.pos = pos
		self.currentFrame = 0
		self.currentAnimation = "default"
		self.timer = 0

		self.animations = {"default": {"frameTime": 1, "frames": []}}

	def update(self, parent):
		"""
		Basic update function.
		:param parent: parent object. Should contain "parent.app.clock.get_time()" function
		"""

		self.timer += parent.app.clock.get_time() / 1000

		frameTime = self.animations[self.currentAnimation]["frameTime"]
		if self.timer > frameTime:
			framesSkipped = int(self.timer // frameTime)
			self.timer %= frameTime

			for _ in range(framesSkipped):
				self.nextFrame()

	def render(self, parent):
		"""
		Basic render function.
		Renders on parent position if self.pos not given
		:param parent: parent object. Should contain "parent.app.screen" object
		:return:
		"""

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
		"""
		Adds new animation to dict
		:param name: name of new animation
		:return:
		"""

		self.animations[name] = [[""]]

	def removeAnimation(self, name):
		"""
		Removes animation from dict
		:param name: name of animation
		:return:
		"""
		self.animations.pop(name)

	def addNewFrame(self, animationName, bitmapFrame=[""]):
		"""
		Adds new bitmap list frame to given animation
		:param animationName: name of animation
		:param bitmapFrame: list in format ["", "", ...]
		:return:
		"""
		self.animations[animationName]["frames"].append(bitmapFrame)

	def removeFrame(self, animationName, frameNumber):
		"""
		Removes frame for given animation by frame number
		:param animationName: name of animation
		:param frameNumber: index of frame
		:return:
		"""
		self.animations[animationName]["frames"].pop(frameNumber)

	def nextFrame(self):
		"""
		Switches frame to next + loops
		:return: Returns -1 if animation have len of 0
		"""
		if len(self.animations[self.currentAnimation]["frames"]) == 0:
			return -1

		self.currentFrame = (self.currentFrame + 1) % len(self.animations[self.currentAnimation]["frames"])

	def prevFrame(self):
		"""
		Switches frame to previous + loops
		:return:
		"""
		self.currentFrame = (self.currentFrame - 1) % len(self.animations[self.currentFrame]["frames"])


	def setCurrentFrame(self, frame):
		"""
		Sets current frame to given
		:param frame: frame number
		:return:
		"""
		self.currentFrame = frame % len(self.animations[self.currentAnimation]["frames"])

	def setCurrentAnimation(self, animationName):
		"""
		Sets animation to given
		:param animationName: name of animation
		:return: Returns -1 if animation not found
		"""
		if animationName not in self.animations.keys():
			return -1
		self.currentAnimation = animationName

		return 0

	def setAnimationFrameTime(self, animationName, frameTime):
		"""
		Sets time to switch frame for given animation
		:param animationName: name of animation
		:param frameTime: time of one frame
		:return:
		"""
		self.animations[animationName]["frameTime"] = frameTime


	def getCurrentAnimationName(self):
		"""
		Returns current animation name
		:return: animation name
		"""
		return self.currentAnimation

	def getCurrentFrameNumber(self):
		"""
		Returns current frame number
		:return: current frame number
		"""
		return self.currentFrame

	def getCurrentAnimation(self):
		"""
		Returns current animation
		:return: Dict {"frameTime": float, "frames": [bitmap lists]}
		"""
		return self.animations[self.currentAnimation]

	def getCurrentFrame(self):
		"""
		Returns current frame bitmap list
		:return: bitmap list
		"""
		return self.animations[self.currentAnimation]["frames"][self.currentFrame]

	def getCurrentFrameTime(self):
		"""
		Returns current frame time
		:return: current frame time
		"""
		return self.animations[self.currentAnimation]["frameTime"]


class Image(UITEMS.Box.Box):
	"""
	Basic Image ui element
	Contains Bitmap object
	"""

	def __init__(self, app, pos=Vector2(0, 0), bitmapFile="Bitmaps/Cursor.bm"):
		super().__init__(app, pos, Vector2(0, 0))

		self.bitmap = Bitmap()
		if bitmapFile is not None:
			self.bitmap.addNewFrame("default", Bitmap.loadBitmap(bitmapFile))

	def update(self):
		"""
		Updates Bitmap object
		:return:
		"""
		self.bitmap.update(self)

	def render(self):
		"""
		Renders Bitmap object
		:return:
		"""
		self.bitmap.render(self)