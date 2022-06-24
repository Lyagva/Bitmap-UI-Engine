from Engine.App import App
from Engine.UiElements.Bitmap import Bitmap
from Engine.Key import Key

from Engine import UiElements

class CustomApp(App):
	def onStart(self):
		print(self.uiElements)

		if "cursor" in self.uiElements.keys():
			self.uiElements["cursor"].bitmap.addNewFrame("default", Bitmap.loadBitmap("Bitmaps/Cursor/Cursor_1.bm"))
			self.uiElements["cursor"].bitmap.nextFrame()
			self.uiElements["cursor"].bitmap.setAnimationFrameTime("default", 0.25)

		if "btn_left" in self.uiElements.keys():
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
					if type(item) == UiElements.Button.Button and item.pos // 16 == gridPos:
						item.onClick()

	def onRender(self):
		pass


customApp = CustomApp()
customApp.run()