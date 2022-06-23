from UITEMS import Bitmap
from pygame import Vector2


def getFilenameByChar(char):
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

def getBitmap(fontName="FONT_4X5", char="a"):
	bitmapItem = Bitmap.Bitmap()

	bitmap = Bitmap.Bitmap.loadBitmap("FONTS/" + fontName + "/" + getFilenameByChar(char))
	if bitmap != -1:
		bitmapItem.addNewFrame("default", bitmap)

	return bitmapItem

def getFontInfo(fontName="FONT_4X5"):
	fontsInfo = {}
	with open("FONTS/info", mode="r") as file:
		for line in file.readlines()[1:]:
			line = line.replace("\n", "").split(";")

			fontsInfo[line[0]] = {}
			fontsInfo[line[0]]["size"] = Vector2(int(line[1]), int(line[2]))

	if fontName in fontsInfo:
		return fontsInfo[fontName]

	return -1