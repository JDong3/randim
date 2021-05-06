from PIL import Image
import random

random.seed(100)

class ImageGenerator:
    def __init__(self, res=(1920, 1080), default_name='pipi'):
        self.name_root = 'xd'
        self.resolution = res

    def create_baseline(self):
        return Image.new('RGB', self.resolution, 'black')

    def create_random(self):
        img = Image.new( 'RGB', (500,500), "black")
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                rands = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                pixels[i,j] = rands
        pass
    def create_squares(self,n):
        img = Image.new( 'RGB', self.resolution, "black")
        pixels = img.load()
        i = 0
        j = 0
        while j < img.size[1]:
            rands = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for ii in range(i, i + n):
                if ii >= img.size[0]:
                    break
                for jj in range(j, j + n):
                    if jj >= img.size[1]:
                        break
                    pixels[ii,jj] = rands
            i = i + n
            if i >= img.size[0]:
                i = 0
                j = j + n
        return img      



ii = ImageGenerator()
ii.create_squares(100).save('xd2.bmp', format='bmp')
