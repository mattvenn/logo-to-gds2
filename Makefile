all: logo_svg.lef logo_svg.gds logo_png.lef logo_png.gds embo.gds

embo.gds: png_2_gds.py embo.png
	python3 $^ $@

logo_svg.gds: svg_2_gds.py logo.svg
	python3 $^ $@

logo_png.gds: png_2_gds.py logo.png 
	python3 $^ $@

view_logo_svg: logo_svg.gds load.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

view_logo_png: logo_png.gds load.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

logo_svg.lef: logo_svg.gds save_svg_lef.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

logo_png.lef: logo_svg.gds save_png_lef.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

clean: 
	rm logo.gds logo.lef

.PHONY: view_logo_svg view_logo_png
