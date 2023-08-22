from PIL import Image
import random
import argparse


def create_black(resolution: tuple[int, int]):
    """
    @param resolution, a 2-tuple of ints, (width, height) of the image
    @return, an Image class of a completely black image
    """
    return Image.new("RGB", resolution, "black")


def create_random(resolution: tuple[int, int]):
    """
    returns an image where each pixel is a randomized color
    """
    image = create_black(resolution)
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            randoms = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            pixels[i, j] = randoms
    return image


def create_squares(self, n):
    """
    I'm not too sure what this does anymore
    """
    img = Image.new("RGB", self.resolution, "black")
    pixels = img.load()
    i = 0
    j = 0
    while j < img.size[1]:
        rands = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        for ii in range(i, i + n):
            if ii >= img.size[0]:
                break
            for jj in range(j, j + n):
                if jj >= img.size[1]:
                    break
                pixels[ii, jj] = rands
        i = i + n
        if i >= img.size[0]:
            i = 0
            j = j + n
    return img


def create_random_greyscale(resolution: tuple[int, int]):
    """
    returns a random image with only grey pixels
    """
    image = create_black(resolution)
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            randomInt = random.randint(0, 255)
            randomInts = (randomInt, randomInt, randomInt)
            pixels[i, j] = randomInts

    return image


def create_big_pixel_random(self, pixel_size=2):
    """
    im not too sure what this does anymore
    """
    img = self.create_black()

    chunks = self._make_chunks(pixel_size)  # list of pixels in a common chunk


def _make_chunks(self, pixel_size=2):
    # for each chunk row
    for i in range(int(self.resolution[1] / 2)):
        for j in range(pixel_size):
            pass

    # do pixel_size # of passes
    # pass


if __name__ == "__main__":
    # stuff = ImageGenerator(res=(300, 300))
    # stuff.create_random().show()
    # stuff.create_random_greyscale().show()
    # stuff.create_big_pixel_random()

    # ii = ImageGenerator()
    # ii.create_squares(100).save('xd2.bmp', format='bmp')

    parser = argparse.ArgumentParser(
        prog="RandIm (Random Image)",
        description="Has some options for generating random images",
        epilog="exmaple, python randim.py --seed abc --type random",
    )

    parser.add_argument(
        "--type",
        help="type of image you want to generate, one of 'black', 'random' or 'randomgreyscale'",
    )
    parser.add_argument("--width", help="width in pixels of the image, ie 1920")
    parser.add_argument("--height", help="height in pixels of the image, ie 1080")
    parser.add_argument(
        "--seed",
        help="a string type seed for the RNG, literally just does random.seed(INPUT_STRING_SEED)",
    )

    parser.add_argument("--output", help="output path, outputs as a bmp")

    args = parser.parse_args()

    print("DEBUG, args are", args)

    if args.seed == None:
        print("no seed provided, using default python random seed")
    else:
        random.seed(args.seed)

    if args.width == None:
        print("no width provided, using default width 1920")
        args.width = 1920

    if args.height == None:
        print("no height provided, using default height 1080")
        args.height = 1080

    if args.output == None:
        print("please provide an output path")
        exit()

    args.width = int(args.width)
    args.height = int(args.height)

    image = None

    match args.type:
        case "black":
            image = create_black((args.width, args.height))
        case "random":
            image = create_random((args.width, args.height))
        case "randomgreyscale":
            image = create_random_greyscale((args.width, args.height))
        case None:
            print("no type provided, using 'random' as type")
            image = create_random((args.width, args.height))
        case _:
            print("invalid --type parameter")

    if not image == None:
        image.save(f"{args.output}", format="bmp")
