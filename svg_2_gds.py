#!/usr/bin/env python3
import gdspy
from PIL import Image
from layers import *
from svgpathtools import svg2paths
import sys

# each square will be 1 um
SCALE=1.0e-6
PIX_SIZE=20 # in units of scale above

# The GDSII file is called a library, which contains multiple cells.
lib = gdspy.GdsLibrary(unit=SCALE)

# Geometry must be placed in cells.
cell = lib.new_cell('LOGO')

# read all paths
paths, attributes = svg2paths(sys.argv[1])
path_num = 0
for path in paths:
    print("processing path #%d" % path_num)
    path_num += 1
    points = []
    for seg in path:
        point = (seg.start.real * PIX_SIZE, -seg.start.imag * PIX_SIZE)
        points.append(point)

    poly = gdspy.Polygon(points, **skywater_metal4)
    cell.add(poly)

lib.write_gds(sys.argv[2])
