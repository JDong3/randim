from PIL import Image
import random
import os

random.seed(100)

class ImageGenerator:
    def __init__(self, res=(1920, 1080), default_name='pipi'):
        self.name_root = name_root
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
                pass
<<<<<<< HEAD

        # do pixel_size # of passes
        pass
=======
>>>>>>> ea214baaae953e2a8e78077c2baf18d1ff7e8fb8

# img.save('xd2.bmp', format='bmp')

if __name__ == "__main__":
    stuff = ImageGenerator(res=(300, 300))
    # stuff.create_random().show()
    # stuff.create_random_greyscale().show()
    stuff.create_big_pixel_random()
    
    ii = ImageGenerator()
    ii.create_squares(100).save('xd2.bmp', format='bmp')
