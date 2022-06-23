from App import App
from UITEMS.Bitmap import Bitmap


class CustomApp(App):
	def onStart(self):
		self.uiElements["cursor"].bitmap.addNewFrame("default", Bitmap.loadBitmap("Bitmaps/Cursor/Cursor_1.bm"))
		self.uiElements["cursor"].bitmap.nextFrame()
		self.uiElements["cursor"].bitmap.setAnimationFrameTime(0.25)

		self.uiElements["btn_left"].onClick = lambda: print("LEFT!")

	def onUpdate(self):
		pass

	def onRender(self):
		pass


customApp = CustomApp()
customApp.run()