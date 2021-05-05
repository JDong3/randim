from PIL import Image
import random

random.seed(100)

class ImageGenerator:
    def __init__(self, res=(1920, 1080), default_name='xd'):
        self.name_root = 'xd'
        self.resolution = res

    def create_baseline(self):
        return Image.new('RGB', res, 'black')

    def create_random(self):
        img = Image.new( 'RGB', (500,500), "black")
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                rands = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                pixels[i,j] = rands
        pass




# img.save('xd2.bmp', format='bmp')
img.show()
