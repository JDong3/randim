from PIL import Image
import random

random.seed(100)

class ImageGenerator:
    def __init__(self, res=(1920, 1080)):
        self.img = Image.new('RGB', res, 'black')

    def create_random(self):
        pass

img = Image.new( 'RGB', (500,500), "black") # Create a new black image
pixels = img.load() # Create the pixel map
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        rands = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # xd = random.randint(0, 255)
        # rands = (xd, xd, xd)
        pixels[i,j] = rands # Set the colour accordingly

# img.save('xd2.bmp', format='bmp')
img.show()
