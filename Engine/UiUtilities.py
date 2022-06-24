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

		element = None

		pos = Vector2(0, 0)
		if "pos" in attrib.keys():
			pos = Vector2(list(map(int, attrib["pos"].split(" "))))

		size = Vector2(0, 0)
		if "size" in attrib.keys():
			size = Vector2(list(map(int, attrib["size"].split(" "))))

		bitmapFile = None
		if "bitmap" in attrib.keys():
			bitmapFile = attrib["bitmap"]

		text = "abcdef"
		if "text" in attrib.keys():
			text = attrib["text"]

		if tag == "box":
			element = Box.Box(app, pos=pos, size=size)

		if tag == "image":
			element = Bitmap.Image(app, pos=pos, bitmapFile=bitmapFile)

		if tag == "button":
			element = Button.Button(app, pos=pos, bitmapFile=bitmapFile)

		if tag == "label":
			element = Label.Label(app, pos=pos, text=text)

		if element:
			elements[attrib["id"]] = element

	return elements