from Engine.UiElements import Bitmap
from pygame import Vector2


def getFilenameByChar(char):
	"""
	Outputs filename by give char
	:param char: single letter
	:return: filename that contains char bitmap
	"""

	filename = "_ERROR"

	# NORMAL CHARACTERS
	if char.lower() in list("qwertyuiopasdfghjklzxcvbnm0123456789 "):
		filename = char

	# SPECIAL CHARACTERS
	specialChars = {"\\": "_back-slash",
				   ":": "_colon",
					",": "_comma",
				   "$": "_dollar",
				   ".": "_dot",
				   "=": "_equal",
				   "!": "_exclamation",
				   "#": "_hashtag",
				   "<": "_left",
					"(": "_left-bracket",
					"[": "_left-bracket-square",
					"-": "_minus",
					"%": "_percent",
					"+": "_plus",
					"?": "_question",
					"\'": "_quote",
					">": "_right",
					")": "_right-bracket",
					"]": "_right-bracket-square",
					";": "_semicolon",
					"/": "_slash",
					"*": "_star",
					"_": "_underline",
					"^": "_up",
					"&": "_ampersand"
					}

	if char in specialChars.keys():
		filename = specialChars[char]

	return filename + ".bm"


def getCharBitmapList(fontName="FONT_4X5", char="a"):
	"""
	Ouputs Bitmap object for given font and char
	:param fontName: Name of font you use
	:param char: single letter that will be outputted as bitmap
	:return: Bitmap class, contains letter .bm image
	"""

	bitmap = [""]

	bitmap = Bitmap.Bitmap.loadBitmap("Engine/FONTS/" + fontName + "/" + getFilenameByChar(char))

	return bitmap

def getFontInfo(fontName="FONT_4X5"):
	"""
	Returns info about given font. If font not found returns -1
	:param fontName: font name
	:return: dictionary: {"size": Vector2(width, height)}
	"""

	fontsInfo = {}
	with open("Engine/FONTS/info", mode="r") as file:
		for line in file.readlines()[1:]:
			line = line.replace("\n", "").split(";")

			fontsInfo[line[0]] = {}
			fontsInfo[line[0]]["size"] = Vector2(int(line[1]), int(line[2]))

	if fontName in fontsInfo:
		return fontsInfo[fontName]

	return -1