import gdspy
from PIL import Image

# each square will be 20 um
SCALE=20.0e-6 

# scale the logo down to 40 x 40 squares
width=40
height=40

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
            rect = gdspy.Rectangle((x, height-y), (x+1, height-y+1))
            cell.add(rect)

# Save the library in a file called 'first.gds'.
lib.write_gds('logo.gds')
