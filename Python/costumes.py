import sys

# Pillow lib/module, majorly used for working with everything, here with
# images. Rather here worked with sorta binary files
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all = True, append_images = [images[1]],
    duration = 200, loop = 0
)