import pygame as pg


class Sound:
	def __init__(self, fileName="Sounds/Laser.wav"):
		self.sound = pg.mixer.Sound(fileName)
		self.volume = 0

	def play(self):
		self.sound.play()

	def stop(self):
		self.sound.stop()

	def mute(self):
		self.sound.set_volume(0)

	def unMute(self):
		self.sound.set_volume(self.volume)

	def setVolume(self, volume):
		self.volume = volume
		self.sound.set_volume(self.volume)

	def getVolume(self):
		return self.volume

	def getLength(self):
		return self.sound.get_length()

	def getRaw(self):
		return self.sound.get_raw()