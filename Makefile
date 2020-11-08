all: logo

logo:
	klayout -l $(PDK_ROOT)/sky130A/libs.tech/klayout/sky130A.lyp logo.gds
