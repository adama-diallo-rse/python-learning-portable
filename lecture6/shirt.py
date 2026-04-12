import sys
from PIL import Image, ImageOps

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input output")

valid = (".jpg", ".jpeg", ".png")
input_ext = sys.argv[1].lower()
output_ext = sys.argv[2].lower()

if not input_ext.endswith(valid) or not output_ext.endswith(valid):
    sys.exit("Invalid input")

if input_ext.split(".")[-1] != output_ext.split(".")[-1]:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
size = shirt.size

input_image = ImageOps.fit(input_image, size)
input_image.paste(shirt, shirt)
input_image.save(sys.argv[2])