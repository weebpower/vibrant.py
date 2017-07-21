
#!/usr/bin/env python3

from colorthief import ColorThief
from sys import argv
from PIL import Image
from colour import Color

MIN_LUM = 0.5
MAX_LUM = 0.9
MIN_SAT = 0.5
WEIGHT_SAT = 3
WEIGHT_LUM = 6
WEIGHT_POP = 1

class Pixel(Color):
    def __init__(self, population, color=None, **kwargs):
        super().__init__(color, **kwargs) 
        self.population = population
    def isvibrant(self):
        return MIN_SAT <= self.saturation and MIN_LUM <= self.luminance <= MAX_LUM
    def vibrance(self):
        return self.population * WEIGHT_POP + self.saturation * WEIGHT_SAT + self.luminance * WEIGHT_LUM
    
def rawcolors_to_objects(imagemap):
    return [Pixel(pixel[1], rgb=pixel[2]) for pixel in imagemap]

def read_hexcodes(file):
    return file.read().splitlines()

def get_palette(imagename):
    ct = ColorThief(argv[1])
    palette = ct.get_palette(quality=1, color_count=32)
    return [Pixel(1, rgb=rgb) for rgb in palette]

def get_colors(imagename):
    im = Image.open(filename).convert('RGB') 
    im.getcolors(0xFFFFFF)

def mostvibrant(colorlist):
    return max(colorlist, key=lambda c: c.vibrance())

def mostvibrant_palette(imagename):
    return mostvibrant(get_palette(imagename))

def mostvibrant_allcolors(imagename):
    return mostvibrant(get_colorcount(imagename))

def main(imagename):
    mostvibrant_allcolors(imagename)

if __name__ == '__main__':
    if len(argv) < 2:
        raise SystemExit('Pass an image as argument.')
    main(argv[1])
