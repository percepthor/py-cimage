import os

import cimage

print ("\nTEST - Image from RGB to gray\n")

original = "images/kitty.jpg"
b_original = original.encode ('utf-8')

output = "images/gray.jpg"
original = "images/kitty.jpg"
b_output = output.encode ('utf-8')

kitty = cimage.image_load_color (b_original, 0, 0)
gray = cimage.image_grayscale (kitty)
cimage.image_save (gray, b_output)