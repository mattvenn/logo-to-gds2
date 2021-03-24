#!/usr/bin/env python3
import gdspy
from PIL import Image
from layers import *
import sys

# each square will be 1 um
SCALE=1.0e-6
PIX_SIZE=20 # in units of scale above

# scale the logo down to 40 x 40 squares
width=75
height=15

im = Image.open(sys.argv[1])
small_im = im.resize((width,height),resample=Image.BILINEAR)

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary(unit=SCALE)

# Geometry must be placed in cells.
cell = lib.new_cell('LOGO')

for x in range(width):
    for y in range(height):
        pix = small_im.getpixel((x,y))
        if pix:
            # Create the geometry (a single rectangle) and add it to the cell.
            rect = gdspy.Rectangle((x * PIX_SIZE, (height-y) * PIX_SIZE), (x * PIX_SIZE + PIX_SIZE, (height-y) * PIX_SIZE + PIX_SIZE), **skywater_metal4)
            cell.add(rect)

lib.write_gds(sys.argv[2])
