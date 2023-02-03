# circuits
## purpose

A python module to help analyze circuits (made to help myself get through my bioinstrumentation class).

## notes

Current focus: analyze circuits with resistors and power sources

- mesh current analysis
	- need to figure out the limitations of MCA
- wire system:
	- each resistor has a 2-element set representing the wires it is connected to
	- each power source has a 2-element ordered pair representing the wires it is connected to
	- all of the resistors in a circuit could be stored in a dictionary where the keys are the wires they are connected to

