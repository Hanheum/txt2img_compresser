from PIL import Image
import numpy as np

image_file_dir = input('image file:')
save_dir = input('save dir:')

image = Image.open(image_file_dir)
width, height = image.size
image = np.array(image)
image = np.reshape(image, [width*height*3])

file = open(save_dir, 'wb')
original_txt = ''
for letter in image:
    original_txt += chr(letter)

file.write(original_txt.encode())