import pygame as pg
from pygame import Vector2, Vector3
import Config


class BitmapPainter:
	"""
	Usage:
		In config file edit:
			BITMAP_PAINTER_ART_SIZE to resolution of your bitmap art
			BITMAP_PAINTER_PIXEL_SIZE to resize every bitmap art pixel to you screen pixel

		Paint with leftMouseButton
		Erase with rightMouseButton

		Save using "s" key. Bitmap art will be saved as "save.bm" at "BitPainter.py" directory
	"""

	def __init__(self):
		self.running = True
		self.events = []
		self.screen = pg.display.set_mode(Config.BITMAP_PAINTER_ART_SIZE * Config.BITMAP_PAINTER_PIXEL_SIZE)
		self.clock = pg.time.Clock()

		self.statistics = {"fps": 0.,
						   "maxFps": 0.,
						   "framesCount": 0,
						   "fpsSum": 0.,
						   "time": 0.}

		self.artSize = Config.BITMAP_PAINTER_ART_SIZE

		self.bitmap = ["0" * int(self.artSize.x) for y in range(int(self.artSize.y))]


	def run(self):
		while self.running:
			self.events = pg.event.get()
			for e in self.events:
				if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
					self.quit()


			# ======== UPDATE ========
			# Paint
			if pg.mouse.get_pressed(3)[0]:
				pos = Vector2(pg.mouse.get_pos()) // Config.BITMAP_PAINTER_PIXEL_SIZE
				self.bitmap[int(pos.y)] = self.bitmap[int(pos.y)][:int(pos.x)] + \
										  "1" + \
										  self.bitmap[int(pos.y)][int(pos.x) + 1:]

			# Erase
			if pg.mouse.get_pressed(3)[2]:
				pos = Vector2(pg.mouse.get_pos()) // Config.BITMAP_PAINTER_PIXEL_SIZE
				self.bitmap[int(pos.y)] = self.bitmap[int(pos.y)][:int(pos.x)] + \
										  "0" + \
										  self.bitmap[int(pos.y)][int(pos.x) + 1:]

			# Save
			if pg.key.get_pressed()[pg.K_s]:
				with open("save.bm", mode="w+") as file:
					saveBitmap = self.bitmap.copy()
					saveBitmap = [f"\'{x}\'" for x in saveBitmap]
					file.write(f"[{', '.join(saveBitmap)}]")


			# ======== RENDER ========
			self.screen.fill((0, 0, 0))

			# GRID
			for x in range(int(self.artSize.x)):
				pg.draw.line(self.screen, (64, 64, 64),
							 (x * Config.BITMAP_PAINTER_PIXEL_SIZE, 0),
							 (x * Config.BITMAP_PAINTER_PIXEL_SIZE,
							  	self.artSize.y * Config.BITMAP_PAINTER_PIXEL_SIZE),
							 2)

			for y in range(int(self.artSize.y)):
				pg.draw.line(self.screen, (64, 64, 64),
							 (0, y * Config.BITMAP_PAINTER_PIXEL_SIZE),
							 (self.artSize.y * Config.BITMAP_PAINTER_PIXEL_SIZE,
							  y * Config.BITMAP_PAINTER_PIXEL_SIZE),
							 2)

			for y, row in enumerate(self.bitmap):
				for x, state in enumerate(row):
					if state == "0":
						continue

					pg.draw.rect(self.screen, (255, 255, 255),
								 pg.Rect((Vector2(x, y)) * Config.BITMAP_PAINTER_PIXEL_SIZE,
										 (Config.BITMAP_PAINTER_PIXEL_SIZE, Config.BITMAP_PAINTER_PIXEL_SIZE)))

			pg.display.flip()

			# ======== FPS =========
			dTime = self.clock.get_time() / 1000
			fps = self.clock.get_fps() * 100 // 1 / 100

			self.statistics["fps"] = fps
			self.statistics["framesCount"] += 1
			self.statistics["maxFps"] = max(self.statistics["maxFps"], fps)
			self.statistics["time"] += dTime
			self.statistics["fpsSum"] += fps

			pg.display.set_caption(f"Python Bitmap Editor by Lyagva - "
								   f"FPS: {fps} - "
								   f"Max FPS: {self.statistics['maxFps']} - "
								   f"Avg FPS: "
								   f"{self.statistics['fpsSum'] / self.statistics['framesCount'] * 100 // 1 / 100} - "
								   f"Time: {self.statistics['time'] * 100 // 1 / 100}")
			self.clock.tick(Config.MAX_FPS)


	def quit(self):
		pg.quit()
		quit()


if __name__ == "__main__":
	app = BitmapPainter()
	app.run()