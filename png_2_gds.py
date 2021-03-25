#!/usr/bin/env python3
import gdspy
from PIL import Image
from layers import *
import sys

# each square will be 1 um
SCALE=1.0e-6
# min area metal 5 is 4mm
PIX_SIZE=2.0 # in units of scale above
# min space is 1.6
PIX_SPACE=PIX_SIZE # + 1.6
PIX_GAP = (PIX_SPACE - PIX_SIZE) / 2

# scale the logo down to 40 x 40 squares
width=50
height=50

im = Image.open(sys.argv[1])
small_im = im.resize((width,height),resample=Image.BILINEAR)
small_im = im.convert('1') # convert image to black and white

width, height = im.size

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary(unit=SCALE)

# Geometry must be placed in cells.
cell = lib.new_cell('LOGO')

for x in range(width):
    for y in range(height):
        pix = small_im.getpixel((x,y))
        print(x, y, pix)
        if pix:
            # Create the geometry (a single rectangle) and add it to the cell.
            rect = gdspy.Rectangle(
                (x * PIX_SPACE + PIX_GAP , (height-y) * PIX_SPACE + PIX_GAP),
                (x * PIX_SPACE + PIX_GAP + PIX_SIZE, (height-y) * PIX_SPACE + PIX_GAP + PIX_SIZE),
                **skywater_metal5)
            cell.add(rect)

lib.write_gds(sys.argv[2])
