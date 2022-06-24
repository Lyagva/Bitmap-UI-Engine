from App import App
from UITEMS.Bitmap import Bitmap
from Key import Key
from Mouse import Mouse

import UITEMS

class CustomApp(App):
	def onStart(self):
		self.uiElements["cursor"].bitmap.addNewFrame("default", Bitmap.loadBitmap("Bitmaps/Cursor/Cursor_1.bm"))
		self.uiElements["cursor"].bitmap.nextFrame()
		self.uiElements["cursor"].bitmap.setAnimationFrameTime("default", 0.25)

		self.uiElements["btn_left"].onClick = lambda: print("You used button with left arrow!")

	def onUpdate(self):
		if "cursor" in self.uiElements.keys():
			pos = self.uiElements["cursor"].pos

			# Move right
			if Key.getKeyDown(Key.Right) and pos.x < 112:
				pos.x += 16
			# Move left
			if Key.getKeyDown(Key.Left) and pos.x > 0:
				pos.x -= 16

			# Move down
			if Key.getKeyDown(Key.Down) and pos.y < 48:
				pos.y += 16
			# Move up
			if Key.getKeyDown(Key.Up) and pos.y > 0:
				pos.y -= 16

			# Interact
			if Key.getKeyDown(Key.Z) or Key.getKeyDown(Key.Space) or Key.getKeyDown(Key.Enter):
				gridPos = pos // 16
				for id, item in self.uiElements.items():
					if type(item) == UITEMS.Button.Button and item.pos // 16 == gridPos:
						item.onClick()

	def onRender(self):
		pass


customApp = CustomApp()
customApp.run()

"""
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
"""