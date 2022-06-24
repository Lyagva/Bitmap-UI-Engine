import pygame as pg

class Key:
	"""
	Class for interacting with keyboard.
	There you can find constants for all available keys.

	Also, there are functions for getting key states like "getKeyDown", "getKeyHold", "getKeyUp"

	Example:
		Key.getKeyDown(keycode=Key.Enter) -> true (If you press Enter on current frame)
	"""
	Enter = pg.K_KP_ENTER
	Esc = pg.K_ESCAPE
	Delete = pg.K_DELETE
	Space = pg.K_SPACE
	Backspace = pg.K_BACKSPACE

	Minus = pg.K_MINUS
	Equals = pg.K_EQUALS
	Slash = pg.K_SLASH
	Backslash = pg.K_BACKSLASH
	Period = pg.K_PERIOD
	Comma = pg.K_COMMA
	Colon = pg.K_COLON
	SemiColon = pg.K_SEMICOLON
	BackQuote = pg.K_BACKQUOTE

	Up = pg.K_UP
	Down = pg.K_DOWN
	Left = pg.K_LEFT
	Right = pg.K_RIGHT

	Shift = pg.KMOD_SHIFT
	Ctrl = pg.KMOD_CTRL
	Alt = pg.KMOD_ALT
	Caps = pg.KMOD_CAPS
	Tab = pg.K_TAB

	Key0 = pg.K_0
	Key1 = pg.K_1
	Key2 = pg.K_2
	Key3 = pg.K_3
	Key4 = pg.K_4
	Key5 = pg.K_5
	Key6 = pg.K_6
	Key7 = pg.K_7
	Key8 = pg.K_8
	Key9 = pg.K_9

	F1 = pg.K_F1
	F2 = pg.K_F2
	F3 = pg.K_F3
	F4 = pg.K_F4
	F5 = pg.K_F5
	F6 = pg.K_F6
	F7 = pg.K_F7
	F8 = pg.K_F8
	F9 = pg.K_F9
	F10 = pg.K_F10
	F11 = pg.K_F11
	F12 = pg.K_F12

	Q = pg.K_q
	W = pg.K_w
	E = pg.K_e
	R = pg.K_r
	T = pg.K_t
	Y = pg.K_y
	U = pg.K_u
	I = pg.K_i
	O = pg.K_o
	P = pg.K_p

	A = pg.K_a
	S = pg.K_s
	D = pg.K_d
	F = pg.K_f
	G = pg.K_g
	H = pg.K_h
	J = pg.K_j
	K = pg.K_k
	L = pg.K_l

	Z = pg.K_z
	X = pg.K_x
	C = pg.K_c
	V = pg.K_v
	B = pg.K_b
	N = pg.K_n
	M = pg.K_m

	@staticmethod
	def getKey(keycode):
		return pg.key.get_pressed()[keycode]
	getKeyHold = getKey

	@staticmethod
	def getKeyPressed(keycode):
		events = pg.event.get(pg.KEYDOWN).copy()
		result = False

		for e in events:
			if e.type == pg.KEYDOWN and e.key == keycode:
				result = True
				break
			pg.event.post(e)

		return result
	getKeyDown = getKeyPressed

	@staticmethod
	def getKeyReleased(keycode):
		events = pg.event.get(pg.KEYUP).copy()
		result = False

		for e in events:
			if e.type == pg.KEYUP and e.key == keycode:
				result = True
				break
			pg.event.post(e)

		return result
	getKeyUp = getKeyReleased