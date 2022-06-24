import pygame as pg

class Mouse:
	LMB = 1
	MMB = 2
	RMB = 3

	@staticmethod
	def getMouse(button):
		return pg.mouse.get_pressed(3)[button]
	getMouseHold = getMouse

	@staticmethod
	def getMousePressed(button):
		events = pg.event.get(pg.MOUSEBUTTONDOWN).copy()
		result = False

		for e in events:
			if e.type == pg.MOUSEBUTTONDOWN and e.button == button:
				result = True
				break
			pg.event.post(e)

		return result
	getMouseDown = getMousePressed

	@staticmethod
	def getMouseRelease(button):
		events = pg.event.get(pg.MOUSEBUTTONUP).copy()
		result = False

		for e in events:
			if e.type == pg.MOUSEBUTTONUP and e.button == button:
				result = True
				break
			pg.event.post(e)

		return result

	getMouseUp = getMouseRelease