# create logos for ASICs with pngs or svgs

turns SVGs or PNGs into GDS2 and LEF files for use on top metal of ASICs for artwork.

![png to gds](docs/png_to_gds.png)

![svg to gds](docs/svg_to_gds.png)

## png

* find/make a suitable png. You will have to work on it to make the final gds be DRC clean.
* png needs to be indexed, 2 colours. white -> gds.
* choose scaling factor (set in program)

## svg

* set inkscape to units px
* make a 1 px grid
* only use 90 or 45 degree angles

# setup

Last tested with MPW8 tagged tools and Magic 8.3 revision 331.

To install MPW8 PDK, follow instructions here: https://github.com/efabless/caravel_user_project/blob/main/docs/source/index.rst#quickstart

