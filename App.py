import UITEMS.Button
from XmlReader import *
import Config
import pygame as pg
from UITEMS.Bitmap import Bitmap

class App:
	def __init__(self):
		"""
		Basic Engine initialization

		Initializes running, events, screen, clock, statistics and uiElements variables
		"""
		self.running = True
		self.events = []
		self.screen = pg.display.set_mode(Config.SCREEN_SIZE * Config.PIXEL_SIZE)
		self.clock = pg.time.Clock()

		self.statistics = {"fps": 0.,
						   "maxFps": 0.,
						   "framesCount": 0,
						   "fpsSum": 0.,
						   "time": 0.}

		self.uiElements = getElementsFromFile(self)

		self.onStart()

	def run(self):
		"""
		Call this to run you app
		Implements basic loop of program with Events, UI update/render and onUpdate()/onDraw() functions
		"""

		while self.running:
			self.events = pg.event.get()
			for e in self.events:
				if e.type == pg.QUIT:
					self.quit()

				if e.type == pg.KEYDOWN and ("cursor" in self.uiElements.keys()):
					if e.key == pg.K_RIGHT and self.uiElements["cursor"].pos.x < 112:
						self.uiElements["cursor"].pos.x += 16
					if e.key == pg.K_LEFT and self.uiElements["cursor"].pos.x > 0:
						self.uiElements["cursor"].pos.x -= 16
					if e.key == pg.K_DOWN  and self.uiElements["cursor"].pos.y < 48:
						self.uiElements["cursor"].pos.y += 16
					if e.key == pg.K_UP  and self.uiElements["cursor"].pos.y > 0:
						self.uiElements["cursor"].pos.y -= 16

					if e.key in [pg.K_SPACE, pg.K_z, pg.K_KP_ENTER]:
						cursorGridPos = self.uiElements["cursor"].pos // 16
						for id, item in self.uiElements.items():
							if type(item) == UITEMS.Button.Button and item.pos // 16 == cursorGridPos:
								item.onClick()


			# ======== UPDATE ========
			for id, element in self.uiElements.items():
				element.update()

			self.onUpdate()

			# ======== RENDER ========
			self.screen.fill((0, 0, 0))

			for id, element in self.uiElements.items():
				element.render()

			self.onDraw()

			pg.display.flip()

			# ======== FPS =========
			self.operateFPS()

	def operateFPS(self):
		"""
		Engine function to work with FPS:
			Count, tick etc.
			Set caption
		"""

		dTime = self.clock.get_time() / 1000
		fps = self.clock.get_fps() * 100 // 1 / 100

		self.statistics["fps"] = fps
		self.statistics["framesCount"] += 1
		self.statistics["maxFps"] = max(self.statistics["maxFps"], fps)
		self.statistics["time"] += dTime
		self.statistics["fpsSum"] += fps

		pg.display.set_caption(f"UI Engine by Lyagva - "
							   f"FPS: {fps} - "
							   f"Max FPS: {self.statistics['maxFps']} - "
							   f"Avg FPS: "
							   f"{self.statistics['fpsSum'] / self.statistics['framesCount'] * 100 // 1 / 100} - "
							   f"Time: {self.statistics['time'] * 100 // 1 / 100}")
		self.clock.tick(Config.MAX_FPS)

	def quit(self):
		"""
		Quits the app
		"""

		pg.quit()
		quit()

	def onStart(self):
		"""
		Overwrite this function
		Calls on startup
		Use to set vars on initialization
		"""
		pass

	def onUpdate(self):
		"""
		Overwrite this function
		Calls every frame
		Use to update vars
		"""
		pass

	def onDraw(self):
		"""
		Overwrite this function
		Calls every frame
		Use to make additional draw
		"""
		pass


if __name__ == "__main__":
	app = App()
	app.run()