import xml.etree.ElementTree as ET

from pygame import Vector2

from Engine.UiElements import Box, Bitmap, Button, Label

def getElementsFromFile(app, filename="layout.xml"):
	"""
	Reads given .xml fileName and returns dictionary with all ui elements
	:param app: main app object
	:param filename: name of .xml fileName with layout (default "layout.xml")
	:return: dictionary with format {id: uiObject}
	"""

	elements = {}

	xmlData = ET.parse(filename)
	root = xmlData.getroot()

	for item in root:
		tag = item.tag
		attrib = item.attrib

		if tag not in ["box", "image", "button", "label"]:
			continue

		id = attrib["id"]

		pos = Vector2(0, 0)
		if "pos" in attrib.keys():
			pos = Vector2(list(map(int, attrib["pos"].split(" "))))


		if tag == "box":
			size = Vector2(0, 0)
			if "size" in attrib.keys():
				size = Vector2(list(map(int, attrib["size"].split(" "))))

			elements[id] = createBox(app, pos=pos, size=size)

		if tag == "label":
			text = "abcdef"
			if "text" in attrib.keys():
				text = attrib["text"]

			font = None
			if "font" in attrib.keys():
				font = attrib["font"]

			elements[id] = createLabel(app, pos=pos, font=font, text=text)


		bitmapFile = None
		if "bitmap" in attrib.keys():
			bitmapFile = attrib["bitmap"]

		if tag == "image":
			elements[id] = createImage(app, pos=pos, defaultBitmapFile=bitmapFile)

		if tag == "button":
			elements[id] = createButton(app, pos=pos, defaultBitmapFile=bitmapFile)


	return elements

def loadBitmap(filename="../Bitmaps/save.bm"):
	"""
	Static method
	Reads fileName and returns bitmap list
	:param filename: Name of .bm fileName
	:return: .bm like list. If fileName not found, returns [""]
	"""

	try:
		with open(filename, mode="r+") as file:
			bitmap = [line.replace("\n", "") for line in file.readlines()]
		return bitmap
	except FileNotFoundError:
		print("File Not Found")
		return [""]


def createBox(app, pos=Vector2(0, 0), size=Vector2(16, 16)):
	return Box.Box(app, pos=pos, size=size)

def createImage(app, pos=Vector2(0, 0), defaultBitmapFile=None):
	return Bitmap.Image(app, pos=pos, bitmapFile=defaultBitmapFile)

def createButton(app, pos=Vector2(0, 0), defaultBitmapFile=None):
	return Button.Button(app, pos=pos, bitmapFile=defaultBitmapFile)

def createLabel(app, pos=Vector2(0, 0), font=None, text="abcdef"):
	return Label.Label(app, pos=pos, font=font, text=text)