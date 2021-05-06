from PIL import Image
import random
import os

random.seed(100)

class ImageGenerator:
    def __init__(self, res=(1920, 1080), name_root='xd'):
        self.name_root = 'xd'
        self.resolution = res

    def generate_name(self):
        stuff = []
        for item in os.listdir('./output'):
            if not item[:len(self.name_root)] == self.name_root:
                stuff.append(item)
        print(stuff)
        pass

    def create_baseline(self):
        return Image.new('RGB', self.resolution, 'black')

    def create_random(self):
        img = self.create_baseline()
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                rands = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                pixels[i,j] = rands

        return img

    def create_random_greyscale(self):
        img = self.create_baseline()
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                xd = random.randint(0, 255)
                rands = (xd, xd, xd)
                pixels[i,j] = rands

        return img

    def create_big_pixel_random(self, pixel_size=2):
        img = self.create_baseline()

        chunks = self._make_chunks(pixel_size) # list of pixels in a common chunk

    def _make_chunks(self, pixel_size=2):
        # for each chunk row
        for i in range(int(self.resolution[1]/2)):
            for j in range(pixel_size):
                
        # do pixel_size # of passes
        pass

# img.save('xd2.bmp', format='bmp')

if __name__ == "__main__":
    stuff = ImageGenerator(res=(300, 300))
    # stuff.create_random().show()
    # stuff.create_random_greyscale().show()
    stuff.create_big_pixel_random()
