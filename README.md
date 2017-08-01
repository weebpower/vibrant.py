# vibrant.py
Extract the most vibrant color in an image.

Two algorithms:
* Get all colors from the image, then pick the most vibrant color from there. More accurate result but usually slower.
* Build a palette using the module `ColorThief`, then pick the most vibrant color from there. More accurate result but usually faster. Less accurate result but faster.

# HOW TO
`$ vibrant.py [-p] IMAGE`

The output will be a single RGB hexcode, such as #48AB4C.

The default is the 'all colors' algorithm. Use the `-p` switch to use the 'palette' algorithm.
