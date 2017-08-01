# vibrant.py
Extract the most vibrant color in an image, using python3.

Two algorithms:
* Get all colors from the image, then pick the most vibrant color from there. More accurate result but usually slower. Requires the `Pillow` module.
* Build a color scheme, then pick the most vibrant color from there. Less accurate result but faster. Requires the `colour` module.

# HOW TO
Install the required modules:

`$ pip3 install Pillow` or `$ pip3 install colour` (see above)

then simply download the file and:

`$ ./vibrant.py [-p] IMAGE`

Please edit the default values at the beginning of the .py file if you don't like the results you get!

The output will be a single RGB hexcode, such as #48AB4C.

The default is the 'all colors' algorithm.  Use the `-p` switch to use the 'palette' algorithm.

# Happy coloring!
