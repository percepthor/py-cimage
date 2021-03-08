from ctypes import Structure, c_int, c_float, c_char_p, POINTER

from .lib import lib

class Image (Structure):
	_fields_ = [
		("w", c_int),
		("h", c_int),
		("c", c_int),
		("data", POINTER (c_float)),
	]

image_load_color = lib.image_load_color
image_load_color.argtypes = [c_char_p, c_int, c_int]
image_load_color.restype = POINTER (Image)

image_save = lib.image_save
image_save.argtypes = [POINTER (Image), c_char_p]
image_save.restype = c_int

image_grayscale = lib.image_grayscale
image_grayscale.argtypes = [POINTER (Image)]
image_grayscale.restype = POINTER (Image)
