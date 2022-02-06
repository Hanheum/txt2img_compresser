import numpy as np
from PIL import Image

input_txt = input('txt:')
save_dir = input('save dir:')
file = open(input_txt, 'rb').read()

image = []
for i in file:
    image.append(int(i))

while len(image)%3 != 0:
    image.append(32)

pixels = int(len(image)/3)
root_pixels = pixels**0.5
round_root_pixels = round(root_pixels)
while root_pixels != round_root_pixels:
    for i in range(3):
        image.append(32)
        pixels = int(len(image) / 3)
        root_pixels = pixels ** 0.5
        round_root_pixels = round(root_pixels)

image = np.array(image)
image = np.reshape(image, [int(root_pixels), int(root_pixels), 3])

image = Image.fromarray(image.astype(np.uint8))

image.save(save_dir)