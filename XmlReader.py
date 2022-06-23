import xml.etree.ElementTree as ET

from pygame import Vector2, Vector3

from UITEMS import Box, Bitmap, Button, Label


def getElementsFromFile(app, filename="layout.xml"):
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