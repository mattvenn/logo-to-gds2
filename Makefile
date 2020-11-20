all: logo

logo.gds: logo.py
	python3 $^

logo: logo.gds
	klayout -l $(PDK_ROOT)/sky130A/libs.tech/klayout/sky130A.lyp $^

logo-magic: logo.gds load.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

logo.lef: logo.gds save_lef.tcl
	magic -rcfile $(PDK_ROOT)/sky130A/libs.tech/magic/sky130A.magicrc $^

clean: 
	rm logo.gds logo.lef

.PHONY: logo-magic
