#!/usr/bin/env python3

from sys import argv, exit
from colour import Color

MINLUM = 0.3
MAXLUM = 0.7
MINSAT = 0.5
WEIGHTSAT = 4.0
WEIGHTLUM = 6.0
WEIGHTPOP = 0.5

# Used to determine the most vibrant color.
class Pixel():
    def __init__(self, population, color=None, **kwargs):
        self.color = Color(color, **kwargs) # see the colour module
        self.population = population        # times it appears in an image
    def __repr__(self):
        return self.color.hex_l
    def vibrance(self):
        return MINSAT <= self.color.saturation and \
	       MINLUM <= self.color.luminance <= MAXLUM and \
               WEIGHTPOP * self.population + \
	       WEIGHTSAT * self.color.saturation + \
	       WEIGHTLUM * absmax1athalf(self.color.luminance) 

# An upside down absolute value function with an absolute maximum of (0.5, 1).
def absmax1athalf(x):
    return (1 - abs(2 * x - 1))

# Program usage. Trivial.
def usage():
    print('USAGE:', __file__, '[-p] IMAGE')
    exit(1)

# Take an rgb color that ranges in [0, 1] and make it range in [0, 255]
def abs_to_rel(rgb):
    return tuple(c / 255 for c in rgb)

# Get a palette from ColorThief, then return it as a list of Pixel objects.
def get_palette(filename, quality, color_count):
    from colorthief import ColorThief
    ct = ColorThief(filename)
    palette = ct.get_palette(quality=quality, color_count=color_count)
    return [Pixel(1, rgb=abs_to_rel(rgb)) for rgb in palette]

# Get all colors from the image and the times they appear using PIL,
# then return them as a list of Pixel objects.
def get_allcolors(filename):
    from PIL import Image
    im = Image.open(filename).convert('RGB')
    imagemap = im.getcolors(0xFFFFFF)
    im.close()
    return [Pixel(pixel[0], rgb=abs_to_rel(pixel[1])) for pixel in imagemap]

# Return the most vibrant color out of an iterable.
def mostvibrant(colorlist):
    return max(colorlist, key=lambda c: c.vibrance())

# The worst but fastest algorithm: get the most vibrant color out of a palette.
def mostvibrant_palette(filename):
    PALETTE_QUALITY = 32     # from 1 to inf. Higher is worse.
    PALETTE_COLOR_COUNT = 32 # from 1 to inf.
    return mostvibrant(get_palette(filename, PALETTE_QUALITY, PALETTE_COLOR_COUNT))

# The best but slowest algorithm: get the most vibrant color out of all pixels.
def mostvibrant_allcolors(filename):
    return mostvibrant(get_allcolors(filename))

def main():
    if len(argv) is 2:
        print(mostvibrant_allcolors(argv[1]))
    elif len(argv) is 3 and '-p' in argv:
        argv.remove('-p')
        print(mostvibrant_palette(argv[1]))
    else:
        usage()

if __name__ == '__main__':
    main()
