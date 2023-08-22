# randim (random image)

## Description

Randim is a python script command line tool that can be used to generate random images based on a few parameters. **Use python 3 please.**

## Test Cases
1. Black image, 400x800 resolution

`python randim.py --type black --width 400 --height 800 --seed asdf --output black.bmp`

2. Random image, 654x456 resolution

`python randim.py --type random --width 654 --height 456 --seed asdf --output random.bmp`

3. Random greyscale image, 1920x1080 resolution

`python randim.py --type randomgreyscale --width 1920 --height 1080 --seed asdf --output randomgreyscale.bmp`
