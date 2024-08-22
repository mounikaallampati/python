import sys
from PIL import Image
images=[]
for arg in sys.argv[1:]:
    image=Image.open(arg)
    images.append(image)
image.save("custumes.gif",save_all=True,append_images=[image[1]],duration=200,loop=0
           )