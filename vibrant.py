#!/usr/bin/env python3

from colorthief import ColorThief
from sys import argv, exit
from PIL import Image
from colour import Color

MIN_LUM = 0.3
MAX_LUM = 0.7
MIN_SAT = 0.4
TARGET_LUM = 0.5
WEIGHT_SAT = 3.0
WEIGHT_LUM = 6.0
WEIGHT_POP = 1.0
PALETTE_QUALITY = 32 # from 1 to inf. Higher is worse.
PALETTE_COLOR_COUNT = 16 # from 1 to inf.

class Pixel():
    def __init__(self, population, color=None, **kwargs):
        self.color = Color(color, **kwargs)
        self.population = population
    def __repr__(self):
        return self.color.hex_l
    def vibrance(self):
        return MIN_SAT <= self.color.saturation and MIN_LUM <= self.color.luminance <= MAX_LUM and \
               self.population * WEIGHT_POP + self.color.saturation * WEIGHT_SAT + \
               abs(self.color.luminance - TARGET_LUM)  * WEIGHT_LUM

def usage():
    print('USAGE:', __file__ + ' [-a] IMAGE')
    exit(1)

def abs_to_rel(rgb):
    return tuple(c / 255 for c in rgb)

def get_palette(filename, quality, color_count):
    ct = ColorThief(filename)
    palette = ct.get_palette(quality=quality, color_count=color_count)
    return [Pixel(1, rgb=abs_to_rel(rgb)) for rgb in palette]

def get_allcolors(filename):
    im = Image.open(filename).convert('RGB')
    imagemap = im.getcolors(0xFFFFFF)
    im.close()
    return [Pixel(pixel[0], rgb=abs_to_rel(pixel[1])) for pixel in imagemap]

def mostvibrant(colorlist):
    return max(colorlist, key=lambda c: c.vibrance())

def mostvibrant_palette(filename, quality, color_count):
    return mostvibrant(get_palette(filename, quality, color_count))

def mostvibrant_allcolors(filename):
    return mostvibrant(get_allcolors(filename))

def main():
    if len(argv) < 2:
        usage()
    elif '-a' in argv:
        argv.remove('-a')
        print(mostvibrant_allcolors(argv[1]))
    else:
        print(mostvibrant_palette(argv[1], PALETTE_QUALITY, PALETTE_COLOR_COUNT))

if __name__ == '__main__':
    main()
