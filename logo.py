#!/usr/bin/env python3
import gdspy
from PIL import Image

# each square will be 1 um
SCALE=1.0e-6
PIX_SIZE=20 # in units of scale above

# scale the logo down to 40 x 40 squares
width=40
height=40

skywater_metal1 = {"layer": 68,  "datatype": 20 }
skywater_metal2 = {"layer": 69,  "datatype": 20 }
skywater_metal3 = {"layer": 70,  "datatype": 20 }
skywater_metal4 = {"layer": 71,  "datatype": 20 }
skywater_metal5 = {"layer": 72,  "datatype": 20 }

im = Image.open("logo.png")
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
            rect = gdspy.Rectangle((x * PIX_SIZE, (height-y) * PIX_SIZE), (x * PIX_SIZE + PIX_SIZE, (height-y) * PIX_SIZE + PIX_SIZE), **skywater_metal5)
            cell.add(rect)

# Save the library in a file called 'first.gds'.
lib.write_gds('logo.gds')
