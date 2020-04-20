import sys
import os
from PIL import Image

#grab first and second arguments
origin = sys.argv[1]
destiny = sys.argv[2]

#check if destiny exists, if not create
if not os.path.exists(destiny):
    os.makedirs(destiny)

#loop through origin
#convert images to png
#save to the new folder
for filename in os.listdir(origin):
    img = Image.open(f'{origin}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{destiny}{clean_name}.png', 'png')
