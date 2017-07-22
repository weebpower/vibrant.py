# vibrant.py
Extract the most vibrant color in an image.

Probably very buggy.

Two methods:

* Build a palette using a module called ColorThief and pick the most vibrant color from there
* Pick the most vibrant color from all colors in the image

They give different colors!

# HOW TO
`$ vibrant.py [-a] IMAGE`

The default is the 'palette' algorithm. The -a switch toggles the 'all' method.
